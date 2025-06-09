import os
import uvicorn
import time
from gradio_interface import app

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    print("Lancement de l'application sur le port", port)
    try:
        uvicorn.run(app, host="0.0.0.0", port=port)
    except Exception as e:
        print("Erreur au lancement de Uvicorn :", e)
    finally:
        print("Processus terminé ?")
        while True:
            time.sleep(10)
