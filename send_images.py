from ultralytics import  YOLO
import cv2
import base64
import requests as rt
from computer_vision import get_frame

# pega os frames da camera
image_list = get_frame()


model = YOLO('../yolov8n-face.pt')  # carrega modelo
i=0
for frame in image_list:
        
    # passa o frame para o modelo
    results =  model(frame)
    frame = results[0].plot()
    # salva o frame
    cv2.imwrite(f"./images/frame.png",frame)
    image = cv2.imread(f"./images/frame.png")
    # converte o frame para base64
    base =base64.b64encode(cv2.imencode('.jpg', image)[1]).decode()
    # envia o frame para o servidor
    print(rt.post("http://127.0.0.1:5000/",json ={"image":base,"name":f"{i}.png"}).json())
    i+=1

