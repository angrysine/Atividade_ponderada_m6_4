from flask import Flask,request
from supabase import create_client
import cv2
from computer_vision  import get_frame
import base64

app = Flask(__name__)
client = create_client(supabase_url="https://rdceolvkjjntkaahmoqj.supabase.co",supabase_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJkY2VvbHZrampudGthYWhtb3FqIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4Njg4NTU3MSwiZXhwIjoyMDAyNDYxNTcxfQ.1j3FalXVDFzt23K4xECzq6_fFIosef1RL45y5T3Tk2c")

@app.get("/")
def hello_world():
    return {"message":"Hello World"}
@app.post("/")
def image():
    try:
        image_string_buffer = bytes(request.get_json()["image"],encoding="utf-8")
        name = request.get_json()["name"]
        image_buffer = base64.b64decode(image_string_buffer)
        with open("image.png","wb") as f:
            f.write(image_buffer)
        response = client.storage.from_("/autoestudo/images").upload(name, "image.png")
        return {"response":str(f"{response}")}
    except Exception as e:
        return {"error":str(e)}


if __name__ == '__main__':
    app.run(debug=True)