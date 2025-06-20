import gradio as gr
import requests
from PIL import Image
import io
import os
from fastapi import FastAPI
from azure.storage.blob import BlobServiceClient

API_URL = "https://webapp-p8-api-awecfjdcg0a3dtgc.francecentral-01.azurewebsites.net/predict"
# Chaîne de connexion
AZURE_STORAGE_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=stockaccountp8;AccountKey=flae3B4NIMDm7xc1N3pmP84VgN+zqnM0+HsGw/Y+OqhfomqVLftO9jy4J5r2aIn+eccsB1G8A147+AStRvQ6TA==;EndpointSuffix=core.windows.net"
CONTAINER_NAME = "projet8"
# Chemins local
LOCAL_DIR = os.path.join(os.getcwd(), "APIData")

app = FastAPI()

# Healthcheck pour éviter l'arrêt automatique
@app.get("/robots933456.txt")
def health_check():
    return "OK"
    
def download_reference_images():
    os.makedirs(LOCAL_DIR, exist_ok=True)

    blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)
    container_client = blob_service_client.get_container_client(CONTAINER_NAME)

    for blob in container_client.list_blobs():
        blob_client = container_client.get_blob_client(blob)
        with open(os.path.join(LOCAL_DIR, os.path.basename(blob.name)), "wb") as f:
            f.write(blob_client.download_blob().readall())

def show_comparison(selected_image_name):
    image_path = LOCAL_DIR + f"{selected_image_name}"
    mask_path = LOCAL_DIR + f"{selected_image_name.replace('leftImg8bit.png', 'gtFine_color.png')}"
    
    # Lecture image et masque
    img = Image.open(image_path)
    real_mask = Image.open(mask_path)

    # Resize image et masque réel
    target_size = (512, 512)
    img_resized = img.resize(target_size, Image.NEAREST)
    real_mask_resized = real_mask.resize(target_size, Image.NEAREST)

    # Prédiction (retourne déjà une image)
    pred_mask_rgb = predict_image(open(image_path, "rb").read())

    # Redimensionner le masque prédit à la taille du masque réel
    pred_mask_resized = pred_mask_rgb.resize(target_size, Image.NEAREST)

    return img_resized, real_mask_resized, pred_mask_resized
    
def predict_image(image_bytes: bytes):
    buffered = io.BytesIO(image_bytes)

    files = {'image': ('image.png', buffered, 'image/png')}
    
    response = requests.post(API_URL, files=files)

    if response.status_code == 200:
        result_image = Image.open(io.BytesIO(response.content))
        return result_image
    else:
        print(f"Erreur {response.status_code} : {response.text}")
        return Image.new("RGB", (256, 256), color="red")  # image rouge si erreur

download_reference_images()
# Liste des fichiers
image_files = sorted(f for f in os.listdir(LOCAL_DIR) if f.endswith("leftImg8bit.png"))

with gr.Blocks() as interface:
    gr.Markdown("## Segmentation Sémantique U-Net")

    dropdown = gr.Dropdown(choices=image_files, label="Choisir une image")

    with gr.Row():
        image = gr.Image(label="Image d'origine")
        mask = gr.Image(label="Masque réel")
        pred = gr.Image(label="Masque prédit")

    dropdown.change(fn=show_comparison, inputs=dropdown, outputs=[image, mask, pred])

# Mount Gradio à la racine
app = gr.mount_gradio_app(app, interface, path="/gradio")
