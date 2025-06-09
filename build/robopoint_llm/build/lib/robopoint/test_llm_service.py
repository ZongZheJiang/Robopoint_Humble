# exists to test run_llm_service.py
from PIL import Image
from run_llm_service import llm_service


image_path = "pic.jpg"
image = Image.open(image_path)
prompt = "Point a location on the table beside the cactus."
while True:
    try:
        output = (llm_service.generate(prompt, images=[image]))
        print(output)
        break
    except Exception as e:
        print('Error, empty input probably')
