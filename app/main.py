#con1
import base64
from fastapi import FastAPI
import cv2
import numpy as np
from pydantic import BaseModel

import requests

class ImageClass(BaseModel):
    image_base64: str
def readb64(uri):
    encoded_data = uri.split(',')[1]
    nparr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)
    return img
    # return encoded_data
def readb641(uri):
    nparr = np.frombuffer(base64.b64decode(uri), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)
    return img
app = FastAPI()

@app.get("/")
def read_root():
    return {"Class animal"}

@app.post("/api/apianimal")
async def read_image(image: ImageClass):
    img =  readb64(image.image_base64)
 
    path_animal = 'http://172.17.0.2:80/api/animal'

    img = cv2.resize(img, (32, 32))
    print(img.shape)
    rimg = img.astype('float32')/255
    retval, buffer = cv2.imencode('.jpg', rimg)
    rimg_base64 = base64.b64encode(buffer).decode('UTF-8')
    
    database64 = {"image_base64":rimg_base64}
    
    headers = {"Content-type": "application/json; charset=UTF-8"}
    img1 =  readb641(database64["image_base64"])
    # img1 =  readb641(database64)
    # print(img1.shape)
    print(img1)
    print("wwwwww")

    animal = requests.post(path_animal, json=database64,headers= headers)
    animal = animal.json()["animal is"]
    print(animal)
    return animal
