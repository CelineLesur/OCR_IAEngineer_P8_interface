
# Projet 8 - Formation IA Engineer d'OpenClassrooms

## Traitez les images pour le système embarqué d’une voiture autonome

### Contexte

Vous êtes ingénieur IA chez "Future Vision Transport", une entreprise qui conçoit des systèmes embarqués de vision par ordinateur pour les véhicules autonomes.

Notre mission est de concevoir un premier modèle de segmentation d’images basé sur le framework Keras.

Ce modèle devra être déployé via une API FastAPI sur le Cloud Azure pour qu'il soit utilisé par les collègues du système de décision.

Cette API prendra en entrée une image et renvoie l'image, le masque réel et le masque préditpar l'API.

### Notebooks complets et commentés ci-dessous :

https://github.com/CelineLesur/OCR_IAEngineer_Projet8/blob/3e2d224de5ef23420196904d508d20d5a4c07417/notebooks/P8_EDA.ipynb

https://github.com/CelineLesur/OCR_IAEngineer_Projet8/blob/3e2d224de5ef23420196904d508d20d5a4c07417/notebooks/P8_DataPreprocessing.ipynb

### Découpage des dossiers :
📂 /

main.py → Code principal de l’API FastAPI

requirements.txt → Liste des packages nécessaires

gradio_interface.py → Script permettant  de créer une interface gradio pour la visualisation de l'image, son masque réel et le masque prédit par l'API

README.md → Explication du contexte du projet, de la hierarchie des fichiers et des packages utilisés

### Installation

#### Prerequisites

Python 3.10

#### Dependencies

- gradio==4.44.1
- gradio_client==1.3.0
- pydantic==2.10.6
- fastapi>=0.100.0
- uvicorn==0.23.0
- requests
- Pillow
- azure-storage-blob
