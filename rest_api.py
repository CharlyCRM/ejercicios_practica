from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel

import asyncio

class UsuarioEntrada(BaseModel):
    id: int
    nombre: str
    email: str

# Modelo para entrada numérica en endpoints asíncronos
class NumeroEntrada(BaseModel):
    numero: int
    incremento: int = 1

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

########################
#   Endpoint POST ASYNC #
########################

@app.post("/calcular/suma")
async def calcular_suma(payload: NumeroEntrada) -> dict:
    """Devuelve numero + incremento (ejemplo de handler asíncrono).
    Simulamos I/O con asyncio.sleep para ilustrar el uso de `await`.
    """
    await asyncio.sleep(0)  # simula una espera no bloqueante
    resultado = payload.numero + payload.incremento
    return {"resultado": resultado}

########################
#   Endpoint GET       #
#######################

@app.get("/usuarios/{id}")
def get_usuario(id: int) -> dict:
    "Devuelve los datos de un usuario"
    for usuario in usuarios:
        if id == usuario["id"]:
            return {
                "id": usuario["id"],
                "nombre": usuario["nombre"],
                "email": usuario["email"]
            }
    return {"error": "El ID indicado no existe"}

    # --- Ejemplo con trabajo en segundo plano (no bloqueante) ---
def guardar_log_suma(n: int, inc: int, res: int) -> None:
    # En un proyecto real, aquí podrías escribir en un fichero, BD, etc.
    print(f"[LOG] Suma recibida: {n} + {inc} = {res}")

@app.post("/calcular/suma_bg")
async def calcular_suma_background(payload: NumeroEntrada, background_tasks: BackgroundTasks) -> dict:
    """Calcula la suma y delega el registro en background."""
    resultado = payload.numero + payload.incremento
    background_tasks.add_task(guardar_log_suma, payload.numero, payload.incremento, resultado)
    return {"resultado": resultado, "info": "Registro en background programado"}

########################
#   Endpoint POST     #
#######################

@app.post("/usuarios")
def crear_usuario(usuario: UsuarioEntrada):
    "Crea un nuevo usuario"
    for u in usuarios:
        if u["id"] == usuario.id:
            return {
                "error": f"❌ El usuario con ID {usuario.id} ya existe: {u['nombre']}"
            }

    usuarios.append(usuario.model_dump())
    return {
        "mensaje": "✅ Usuario creado correctamente",
        "usuario": usuario.model_dump()
    }

########################
#   Endpoint PUT       #
########################

@app.put("/usuarios/{id}")
def actualizar_usuario(id: int, usuario_actualizado: UsuarioEntrada):
    "Actualiza completamente los datos de un usuario existente"
    for index, usuario in enumerate(usuarios):
        if usuario["id"] == id:
            usuarios[index] = usuario_actualizado.model_dump()
            return {
                "mensaje": f"🔄 Usuario {id} actualizado correctamente",
                "usuario": usuarios[index]
            }
    return {"error": f"❌ No se encontró un usuario con ID {id}"}

########################
#   Endpoint DELETE    #
########################

@app.delete("/usuarios/{id}")
def eliminar_usuario(id: int):
    "Elimina un usuario por su ID"
    for i, usuario in enumerate(usuarios):
        if usuario["id"] == id:
            usuarios.pop(i)
            return {"mensaje": f"🗑️ Usuario con ID {id} eliminado correctamente"}
    return {"error": f"❌ No existe ningún usuario con ID {id}"}


# Ejecución
# uvicorn rest_api:app --reload  
# # rest_api - hace referencia al nombre del fichero
# # app es el nombre de la instancia de FastAPI
# # --reload reinicia el servidor automáticamente cuando haces cambios
#   http://127.0.0.1:8000/docs → verás la documentación interactiva
#   http://127.0.0.1:8000/redoc → otra vista de documentación generada

# Ejecución para que otro dispositivo de la red se conecte
# Obtener la IP del ordenador
# ipconfig getifaddr en0
# Laznar el servidor
# curl http://192.168.1.42:8000/

# Ejemplo de POST o PUT
# curl -X POST http://127.0.0.1:8000/usuarios/2 \
#      -H "Content-Type: application/json" \
#      -d '{"id": 2, "nombre": "Daniela", "email": "daniela_nueva@mail.com"}'

# Ejemplos ASYNC
# curl -X POST http://127.0.0.1:8000/calcular/suma \
#      -H "Content-Type: application/json" \
#      -d '{"numero": 7, "incremento": 5}'
#
# curl -X POST http://127.0.0.1:8000/calcular/suma_bg \
#      -H "Content-Type: application/json" \
#      -d '{"numero": 10, "incremento": 2}'