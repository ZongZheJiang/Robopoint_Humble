# This is the standalone script - the script has been adapted to run in ros as a class in run_llm_service.py
#
# Run this script as a sanity check - it will change annotated_pic.jpg and print the 2d points and boxes
import torch
from PIL import Image, ImageDraw
import re, base64
from robopoint.mm_utils import process_images, load_image_from_base64, tokenizer_image_token
from robopoint.constants import DEFAULT_IMAGE_TOKEN, DEFAULT_IM_START_TOKEN, DEFAULT_IM_END_TOKEN, IMAGE_TOKEN_INDEX
from robopoint.model.builder import load_pretrained_model
from robopoint.utils import disable_torch_init


# LoRA only works without quantization, therefore I merged the full model with the LoRA adapter then uploaded it
# model_name = "llava-llama-2-7b-lora"
# model_base = "meta-llama/Llama-2-7b-chat-hf"
# model_path = "wentao-yuan/robopoint-v1-llama-2-7b-lora"

# you can also try this model, but its 13b.
# model_name = "robopoint-v1-vicuna-v1.5-13b"
# model_base= None
# model_path = "wentao-yuan/robopoint-v1-vicuna-v1.5-13b"

model_name = "llava-llama-2-7b-johnwee1" # arbitrary name is ok
model_base = None
model_path = "johnwee1/robopoint-v1-llama-2-7b"

disable_torch_init()
# Function to load the model
tokenizer, model, image_processor, context_len = load_pretrained_model(model_path, model_base, model_name)

@torch.inference_mode()
def generate(tokenizer, model, image_processor, prompt, images=None, temperature=1.0, top_p=1.0, max_new_tokens=256):
    # Process images if provided
    if images is not None and len(images) > 0:
        if len(images) != prompt.count(DEFAULT_IMAGE_TOKEN):
            raise ValueError("Number of images does not match number of <image> tokens in prompt")

        images = [load_image_from_base64(image) for image in images]
        image_sizes = [image.size for image in images]
        images = process_images(images, image_processor, model.config).to(model.device, dtype=torch.float16)

        # if isinstance(images, list):
        #     images = [image.to(model.device, dtype=torch.float16) for image in images]
        # else:
        #     images = images.to(model.device, dtype=torch.float16)

        # replace_token = DEFAULT_IMAGE_TOKEN
        # if getattr(model.config, 'mm_use_im_start_end', False):
        #     replace_token = DEFAULT_IM_START_TOKEN + replace_token + DEFAULT_IM_END_TOKEN
        # prompt = prompt.replace(DEFAULT_IMAGE_TOKEN, replace_token)

        image_args = {"images": images, "image_sizes": image_sizes}
    else:
        image_args = {}

    # Prepare input
    input_ids = tokenizer_image_token(prompt, tokenizer, IMAGE_TOKEN_INDEX, return_tensors='pt').unsqueeze(0).to(model.device)
    # Generate
    do_sample = True if temperature > 0.001 else False
    outputs = model.generate(
        inputs=input_ids,
        images=images,
        image_sizes=image_sizes,
        do_sample=do_sample,
        temperature=temperature,
        top_p=top_p,
        max_new_tokens=max_new_tokens,
        use_cache=True,
    )

    # Debug information
    # vision_tower = model.get_vision_tower()
    # print("Vision tower loaded:", vision_tower.is_loaded)
    # print(f"Type of model:{type(model)}")
    # print("Vision tower model:", model.config.mm_vision_tower)
    # print("Image processor:", type(image_processor))
    # from transformers import AutoConfig
    # config = AutoConfig.from_pretrained(model_path)
    # print(f"Config: {config.model_type}")
    # print(f"Config: {config.architectures}")
    #

    # Decode and return the generated text
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return generated_text

# images are passed as base64 strings
def encode_image(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def find_vectors(text):
    pattern = r"\(([-+]?\d+\.?\d*(?:,\s*[-+]?\d+\.?\d*)*?)\)"
    matches = re.findall(pattern, text)
    vectors = []
    for match in matches:
        vector = [float(num) if '.' in num else int(num) for num in match.split(',')]
        vectors.append(vector)
    return vectors

def visualize_2d(img, points, bounding_boxes, scale=1.0, cross_size=9, cross_width=4):
    if img.mode != 'RGBA':
        img = img.convert('RGBA')

    draw = ImageDraw.Draw(img)
    size = int(cross_size * scale)
    width = int(cross_width * scale)

    # Draw points
    for x, y in points:
        draw.line((x - size, y - size, x + size, y + size), fill='red', width=width)
        draw.line((x - size, y + size, x + size, y - size), fill='red', width=width)

    # Draw bounding boxes
    for x1, y1, x2, y2 in bounding_boxes:
        draw.rectangle([x1, y1, x2, y2], outline='red', width=width)

    img = img.convert('RGB')
    return img

image_path = "pic.jpg"
original_image = Image.open(image_path)
image = encode_image(image_path)
pre = """[INST]\n<image>.\n"""
post = " Your answer should be formatted as a list of tuples, " \
        "i.e. [(x1, y1), (x2, y2), ...], where each tuple contains the " \
        "x and y coordinates of a point satisfying the conditions above." \
        " The coordinates should be between 0 and 1, indicating the " \
        "normalized pixel locations of the points in the image. [/INST]"
prompt = pre + "Point to a spot on the dressing table." + post
output = generate(tokenizer, model, image_processor, prompt, images=[image])
print(output)
vectors = find_vectors(output)
print(f"Vector output: {vectors}")

def process_and_visualize_output(output_text, original_image, output_path=None):
    """
    Returns:
        tuple: (annotated_image, vectors_2d, vectors_bbox)
            - annotated_image (PIL.Image): Image with drawn points/boxes
            - vectors_2d (list): List of (x,y) points found in output
            - vectors_bbox (list): List of (x1,y1,x2,y2) boxes found in output
    """
    width, height = original_image.size

    # Process the output to find vectors
    vectors = find_vectors(output_text)
    print("Found vectors:", vectors)

    # Separate 2D points and bounding boxes
    vectors_2d = [vec for vec in vectors if len(vec) == 2]
    vectors_bbox = [vec for vec in vectors if len(vec) == 4]
    print(f"Found {len(vectors_2d)} 2D points and {len(vectors_bbox)} bounding boxes")

    # Scale normalized coordinates to image dimensions
    scaled_points = []
    for x, y in vectors_2d:
        if isinstance(x, float) and x <= 1:
            x = x * width
            y = y * height
        scaled_points.append((x, y))

    scaled_bbox = []
    for x1, y1, x2, y2 in vectors_bbox:
        if isinstance(x1, float) and x1 <= 1:
            x1 = x1 * width
            y1 = y1 * height
            x2 = x2 * width
            y2 = y2 * height
        scaled_bbox.append((x1, y1, x2, y2))

    # Create annotated image
    annotated_image = visualize_2d(
        original_image.copy(),
        scaled_points,
        scaled_bbox,
        scale=1.0  # Adjust scale as needed
    )

    # Save the annotated image if path is provided
    if output_path:
        annotated_image.save(output_path)
        print(f"Annotated image saved to {output_path}")

    return annotated_image, vectors_2d, vectors_bbox
annotated_image, pts, boxes = process_and_visualize_output(output, original_image, output_path="annotated_pic.jpg")
print(f"2d points: {pts}")
print(f"boxes: {boxes}")
