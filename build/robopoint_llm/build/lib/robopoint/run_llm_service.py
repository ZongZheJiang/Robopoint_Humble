# I copied the code from run_llm.py and modify it so that it can be called by query.
from typing import List, Union
import torch
from PIL import Image, ImageDraw
import re, base64
from robopoint.mm_utils import process_images, load_image_from_base64, tokenizer_image_token
from robopoint.constants import DEFAULT_IMAGE_TOKEN, DEFAULT_IM_START_TOKEN, DEFAULT_IM_END_TOKEN, IMAGE_TOKEN_INDEX
from robopoint.model.builder import load_pretrained_model
from robopoint.utils import disable_torch_init


# model is REALLY sensitive to the prompt format, so we need to make sure the prompt is in the correct format
# this is the prompt format for LLAMA2. Different from vicuna
# Taken from eval/run_llava.py
pre = """[INST] <<SYS>>
You are a helpful language and vision assistant. You are able to understand the visual content that the user provides, and assist the user with a variety of tasks using natural language.
<</SYS>>\n\n<image>.\n"""
post = " Your answer should be formatted as a list of tuples, " \
        "i.e. [(x1, y1), (x2, y2), ...], where each tuple contains the " \
        "x and y coordinates of a point satisfying the conditions above." \
        " The coordinates should be between 0 and 1, indicating the " \
        "normalized pixel locations of the points in the image. [/INST]"


# model_name = "llava-llama-2-7b-lora"
# model_base = "meta-llama/Llama-2-7b-chat-hf"
# model_path = "wentao-yuan/robopoint-v1-llama-2-7b-lora"

model_name = "llava-llama-2-7b"
model_base = None
model_path = "johnwee1/robopoint-v1-llama-2-7b"


class LLMService:
    def __init__(self):
        disable_torch_init()
        self.tokenizer, self.model, self.image_processor, self.context_len = load_pretrained_model(model_path, model_base, model_name, load_4bit=True)
        print("context length:")
        print(self.context_len)

    def _find_vectors(self, text):
        """
        Find vectors in the text that match the pattern "(x1, y1, ..., xn, yn)"
        However, in the original robopoint code, it could return multiple vector matches.
        For the purposes of the Robopoint demo we only care about the first match.
        """
        pattern = r"\(([-+]?\d+\.?\d*(?:,\s*[-+]?\d+\.?\d*)*?)\)"
        matches = re.findall(pattern, text)
        vectors = []
        for match in matches:
            vector = [float(num) for num in match.split(',')]
            vectors.append(vector)
        return vectors[0] # this returns [x, y] ONLY !

    @torch.inference_mode()
    def generate(self, prompt, images: Union[List[Image.Image],None]=None, temperature=1.0, top_p=1.0, max_new_tokens=256):
        prompt = pre+prompt+post
        print("Prompt:", prompt)
        # Process images if provided
        if images is not None and len(images) > 0:
            if len(images) != prompt.count(DEFAULT_IMAGE_TOKEN):
                raise ValueError("Number of images does not match number of <image> tokens in prompt")

            # images = [load_image_from_base64(image) for image in images] # Load images from base64, but no need if CV bridge is used
            images = [image.convert("RGB") for image in images]
            image_sizes = [image.size for image in images]
            images = process_images(images, self.image_processor, self.model.config)

            if isinstance(images, list):
                images = [image.to(self.model.device, dtype=torch.float16) for image in images]
            else:
                images = images.to(self.model.device, dtype=torch.float16)

            replace_token = DEFAULT_IMAGE_TOKEN
            if getattr(self.model.config, 'mm_use_im_start_end', False):
                replace_token = DEFAULT_IM_START_TOKEN + replace_token + DEFAULT_IM_END_TOKEN
            prompt = prompt.replace(DEFAULT_IMAGE_TOKEN, replace_token)

            image_args = {"images": images, "image_sizes": image_sizes}
        else:
            image_args = {}

        # Prepare input
        input_ids = tokenizer_image_token(prompt, self.tokenizer, IMAGE_TOKEN_INDEX, return_tensors='pt').unsqueeze(0).to(self.model.device)

        # Generate
        do_sample = True if temperature > 0.001 else False

        # hack: if generated text is empty, keep generating until we get something
        generated_text = ""
        while not generated_text:
            outputs = self.model.generate(
                inputs=input_ids,
                do_sample=do_sample,
                temperature=temperature,
                top_p=top_p,
                max_new_tokens=max_new_tokens,
                use_cache=True,
                **image_args
            )

            # Decode and return the generated text
            generated_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
        return self._find_vectors(generated_text)

    def _visualize_2d(self, img, points, bounding_boxes, scale=1.0, cross_size=9, cross_width=4):
        '''Not used yet: Internal function to draw 2D crosses on the image'''
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


    def process_and_visualize_output(self, output_vector, original_image, output_path=None):
        """
        Not used yet
        Returns:
            tuple: (annotated_image, vectors_2d, vectors_bbox)
                - annotated_image (PIL.Image): Image with drawn points/boxes
                - vectors_2d (list): List of (x,y) points found in output
                - vectors_bbox (list): List of (x1,y1,x2,y2) boxes found in output
        """
        width, height = original_image.size

        # Process the output to find vectors
        vectors = [output_vector]
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
        annotated_image = self._visualize_2d(
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

llm_service = LLMService()
print("LLMService initialized - ready to accept requests now")
