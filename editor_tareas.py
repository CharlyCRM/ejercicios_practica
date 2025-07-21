# ===========================================
# 💻 GESTOR DE TAREAS EN PYTHON
# ===========================================

# Tareas a realizar:
# 1. Mostrar un menú con opciones hasta que el usuario decida salir.
# 2. Permitir al usuario:
#    - Ver la lista de tareas y su estado (pendiente o completada).
#    - Añadir nuevas tareas al listado.
#    - Marcar una tarea como completada.
#    - Eliminar una tarea de la lista.
#    - Guardar las tareas en un archivo de texto.
#    - Cargar las tareas desde un archivo de texto.
# 3. Usar un bucle `while` para mantener el menú activo.
# 4. Usar listas de diccionarios para representar las tareas.
# 5. Usar funciones para organizar el código (una función por opción).
# 6. Utilizar `input()` para recibir instrucciones del usuario.
# 7. Implementar manejo de errores con `try/except` donde sea necesario.

import os
import json

def limpiar_terminal():
    os.system('cls' if os.name == 'nt'else 'clear')

tareas = []

def mostrar_menu():
    print("\n--- MENÚ GESTOR DE TAREAS ---")
    print("1. Ver tareas")
    print("2. Añadir tarea")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Guardar tareas en archivo")
    print("6. Cargar tareas desde archivo")
    print("7. Salir")

while True:
    mostrar_menu()
    try:
        opcion = int(input("Elige una opción (1-7): "))
    except ValueError:
        print(f"❌ Por favor, introduce un número del 1 al 7")
        continue
        

    if opcion == 1:
        limpiar_terminal()
        print(f"\n--- VER TAREAS ---")
        
        for i, tarea in enumerate(tareas, start=1):
            estado = "✅ Completada" if tarea["completada"] else "⏳ Pendiente"
            print(f"\n{i}. {tarea['nombre'].capitalize()} - {estado}")
            print(f"   Descripción: {tarea['descripcion']}")

    
    elif opcion == 2:
        limpiar_terminal()
        print(f"\n--- AGREGAR NUEVA TAREA ---")

        nueva_tarea = input("Título de la tarea: ").lower()
        nueva_descripcion = input("Describa la tarea: ").lower()

        nueva = {
            "nombre": nueva_tarea,
            "descripcion": nueva_descripcion,
            "completada": False
            }
        tareas.append(nueva)
        print(f"✅ La tarea {nueva_tarea} ha sido agregada correctamente") 

    
    elif opcion == 3:
        limpiar_terminal()
        print(f"\n--- MARCAR TAREA COMO COMPLETADA ---")

        if not tareas:
            print("⚠️ No hay tareas para marcar.")
            continue

        for i, tarea in enumerate(tareas, start=1):
            estado = "✅" if tarea["completada"] else "⏳"
            print(f"{i}. {tarea['nombre'].capitalize()} - {estado}")

        try:
            tarea_completada = int(input("\nIndique el número de la tarea completada: "))
            if 1 <= tarea_completada <= len(tareas):
                tareas[tarea_completada - 1]["completada"] = True
                print(f"✅ Tarea '{tareas[tarea_completada - 1]['nombre']}' marcada como completada.")
            else:
                print("❌ Número fuera de rango.")
        except ValueError:
            print("❌ Debes introducir un número válido.")

    
    elif opcion == 4:
        limpiar_terminal()
        print(f"\n--- ELIMINAR UNA TAREA ---")

        if not tareas:
            print(f"⚠️ No hay tareas para eliminar.")
            continue

        for i, tarea in enumerate(tareas, start=1):
            estado = "✅ Completada" if tarea["completada"] else "⏳"
            print(f"{i}. {tarea['nombre'].capitalize()} - {estado}")

        try:
            tarea_eliminar = int(input("\nIndique el número de la tarea a eliminar: "))
            if 1 <= tarea_eliminar <= len(tareas):
                tarea_borrada = tareas.pop(tarea_eliminar - 1)
                print(f"✅ Tarea '{tarea_borrada['nombre']}' eliminada correctamente.")
            else:
                print(f"❌ Número fuera de rango.")
        except ValueError:
            print("❌ Debes introducir un número válido.")

    
    elif opcion == 5:
        limpiar_terminal()
        print(f"\n--- GUARDAR TAREA EN ARCHIVO ---")

        try:
            with open("tareas.json", "w", encoding="utf8") as archivo:
                json.dump(tareas, archivo, indent=4, ensure_ascii=False)
            print(f"✅ Tareas guardadas correctamente en 'tareas.json")
        except Exception as e:
            print(f"❌ Error al guardar las tareas: {e}")

    
    elif opcion == 6:
        limpiar_terminal()
        print(f"\n--- CARGAR TAREAS DESDE ARCHIVO ---")

        try:
            with open("tareas.json", "r", encoding="utf8") as archivo:
                tareas = json.load(archivo)
            print("✅ Tareas cargadas correctamente desde tareas.json'")
        except FileNotFoundError:
            print(f"⚠️ No se encontró el archivo 'tareas.json'")
        except json.JSONDecodeError:
            print(f"❌ El archivo existe pero está dañado o vacio")
        except Exception as e:
            print(f"❌ Error al cargar el fichero {e}")

        
    elif opcion ==  7:
        limpiar_terminal()
        print(f"¡Gracias por usar nuestra aplicación! Hasta pronto. 😊")
        break
    
    else:
        limpiar_terminal()
        print("❌ Opción no válida. Por favor, selecciona un número del 1 al 7")
