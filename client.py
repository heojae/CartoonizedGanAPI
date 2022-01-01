import requests
import PIL
from io import BytesIO
from PIL import Image

url = 'http://localhost:8080/cartoonize'
files = {'image': open('./sample/a.png', 'rb')}


response = requests.post(url, files=files)
print("------------------------ Response 받기 완료 ------------------------")


image_bytes: bytes = response.content
data_io = BytesIO(image_bytes)
img: PIL.Image.Image = Image.open(data_io)
img.save("./sample/jit_cg_a.jpeg")
print("------------------------- 이미지 저장 완료 -------------------------")
