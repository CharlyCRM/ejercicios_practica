
from fastapi import FastAPI

app = FastAPI()

usuarios = [
    {
        "id": 1,
        "nombre": "Carlos",
        "email": "charlycrm@hotmail.com"
    },
    {
        "id": 2,
        "nombre": "Dania",
        "email": "danielamaya@hotmail.com"
    }
]

@app.get("/")
def leer_root():
    return usuarios


# Ejecución
# uvicorn rest_api:app --reload  
# rest_api - hace referencia al nombre del fichero
# app es el nombre de la instancia de FastAPI
# --reload reinicia el servidor automáticamente cuando haces cambios
#   http://127.0.0.1:8000/docs → verás la documentación interactiva
#   http://127.0.0.1:8000/redoc → otra vista de documentación generada

# Ejecución para que otro dispositivo de la red se conecte
# Obtener la IP del ordenador
# ipconfig getifaddr en0
# Laznar el servidor
# curl http://192.168.1.42:8000/