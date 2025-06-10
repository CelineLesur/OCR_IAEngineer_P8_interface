import gradio as gr
import requests
from PIL import Image
import io
import os
from fastapi import FastAPI

from fastapi import FastAPI
import gradio as gr
from PIL import Image
import io
import requests

API_URL = "https://webapp-p8-api-awecfjdcg0a3dtgc.francecentral-01.azurewebsites.net/predict"

app = FastAPI()

# Healthcheck pour éviter l'arrêt automatique
@app.get("/robots933456.txt")
def health_check():
    return "OK"


def predict_image(image: Image.Image):
    return "Image reçue avec succès"
    
# Gradio Interface
# def predict_image(image: Image.Image):
#     try:
#         buffered = io.BytesIO()
#         image.save(buffered, format="PNG")
#         buffered.seek(0)
#         files = {'image': ('image.png', buffered, 'image/png')}
#         response = requests.post(API_URL, files=files)
#         if response.status_code == 200:
#             return Image.open(io.BytesIO(response.content))
#         else:
#             return f"Erreur {response.status_code} : {response.text}"
#     except Exception as e:
#         return f"Erreur interne : {e}"
print("INPUTS type:", type(gr.Image(type="pil")))
print("OUTPUTS type:", type(gr.Textbox(label="Sortie debug")))

interface = gr.Interface(
    fn=predict_image,
    inputs=gr.Image(type="pil", label="Télécharge une image"),
    outputs=gr.Textbox(label="Sortie debug"), #debug
    # outputs=gr.Image(type="pil", label="Image segmentée"),
    allow_flagging="never",
    title="Segmentation Sémantique U-Net",
    description="Ce modèle applique une segmentation sémantique avec U-Net sur les images urbaines."
)

# Mount Gradio à la racine
app = gr.mount_gradio_app(app, interface, path="/gradio")
