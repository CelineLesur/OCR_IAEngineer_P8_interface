import gradio as gr
import requests
from PIL import Image
import io
import os
from fastapi import FastAPI

API_URL = "https://webapp-p8-api-awecfjdcg0a3dtgc.francecentral-01.azurewebsites.net/predict"  
def predict_image(image: Image.Image):
    try:
        buffered = io.BytesIO()
        image.save(buffered, format="PNG")
        buffered.seek(0)

        files = {'image': ('image.png', buffered, 'image/png')}

        response = requests.post(API_URL, files=files)

        if response.status_code == 200:
            result_image = Image.open(io.BytesIO(response.content))
            return result_image
        else:
            print(f"Erreur {response.status_code} : {response.text}")
            return f"Erreur {response.status_code} : {response.text}"
    except Exception as e:
        print(f"Exception dans predict_image: {e}")
        return f"Erreur interne : {e}"

# Interface Gradio
interface = gr.Interface(
    fn=predict_image,
    inputs=gr.Image(type="pil", label="Télécharge une image"),
    outputs=gr.Image(type="pil", label="Image segmentée"),
    allow_flagging="never",
    title="Segmentation Sémantique U-Net",
    description="Ce modèle applique une segmentation sémantique avec U-Net sur les images urbaines."
)

app = FastAPI()
app = gr.mount_gradio_app(app, interface, path="/")

