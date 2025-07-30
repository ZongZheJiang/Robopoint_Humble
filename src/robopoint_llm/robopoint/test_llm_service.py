# exists to test run_llm_service.
from PIL import Image
from run_llm_service import llm_service

image_path = "./pic.jpg"
image = Image.open(image_path)
print(image)
prompt = "Point a location on the table beside the cactus."
while True:
    try:
        output = (llm_service.generate(prompt, images=[image]))
        print(output)

        annotated_image, points, bboxes = llm_service.process_and_visualize_output(
        output, 
        image.copy(),  # Pass a copy of the original image
        output_path="./annotated_pic.jpg" # Tell it where to save the new image
        )
        annotated_image.show()


        break
    except Exception as e:
        print('Error, empty input probably')
