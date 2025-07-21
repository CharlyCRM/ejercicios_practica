# ===========================================
# 📅 EJERCICIO: AGENDA DE CONTACTOS EN PYTHON
# ===========================================

# Tareas a realizar:
# 1. Mostrar un menú con opciones hasta que el usuario decida salir.
# 2. Permitir al usuario:
#    - Ver todos los contactos con nombre, teléfono y correo.
#    - Añadir un nuevo contacto (con validación de nombre duplicado).
#    - Buscar contactos por nombre (coincidencia parcial).
#    - Editar un contacto existente (cambiar nombre, teléfono o correo).
#    - Eliminar un contacto.
#    - Guardar la agenda en un archivo de texto.
#    - Cargar la agenda desde un archivo.
# 3. Usar un bucle `while` para mantener el menú activo.
# 4. Usar listas de diccionarios para representar los contactos.
# 5. Usar funciones para organizar el código (una función por opción).
# 6. Utilizar `input()` para recibir instrucciones del usuario.
# 7. Implementar manejo de errores con `try/except` donde sea necesario.


import os
import json

def limpiar_terminal():
    os.system('cls' if os.name == 'nt'else 'clear')

contactos = [] # Diccionario anidado en una lista

def mostrar_menu():
    print("\n--- MENÚ AGENDA DE CONTACTOS ---")
    print("1. Ver contactos")
    print("2. Añadir nuevo contacto")
    print("3. Buscar contacto")
    print("4. Editar contacto")
    print("5. Eliminar contacto")
    print("6. Guardar agenda")
    print("7. Cargar agenda")
    print("8. Salir")

while True:
    mostrar_menu()
    try:
        opcion = int(input("Seleccione una opción (1 - 8): "))
    except ValueError:
        limpiar_terminal()
        print(f"❌ Por favor, introduce un número del 1 al 8")
        continue
    
    if opcion == 1:
        limpiar_terminal()
        print(f"\n--- VER CONTACTOS ---")

        for i, contacto in enumerate(contactos, start=1):
            print(f"{i}. Nombre: {contacto['nombre'].capitalize()}")
            print(f"   Teléfono: {contacto['telefono']}")
            print(f"   Email: {contacto['email']}\n")
        
        if  not contactos:
            print("La agenda está vacia")


    if opcion == 2:
        limpiar_terminal()
        print(f"\n--- AÑADIR CONTACTO ---")
        
        nombre = input("Nombre del contacto: ").lower()
        telefono = input("Teléfono: ")
        email = input("Correo electrónico: ").lower()

        # Validar duplicado
        if any(c["nombre"] == nombre for c in contactos):
            print(f"⚠️ Ya existe un contacto con el nombre '{nombre}'")
        else:
            contactos.append({ # Creación de diccionario dentro de la lista contactos
                "nombre": nombre,
                "telefono": telefono,
                "email": email
            })
            print(f"✅ Contacto '{nombre}' añadido correctamente.")

    elif opcion == 3:
        limpiar_terminal()
        print(f"\n--- BUSCAR CONTACTO POR NOMBRE ---")

        buscar_nombre = input("Introduce parte del nombre a buscar: ").lower()
        encontrados = []

        for i, contacto in enumerate(contactos, start=1):
            if buscar_nombre in contacto["nombre"]:
                encontrados.append((i, contacto))

        if encontrados:
            for i, contacto in encontrados:
                print(f"{i}. Nombre: {contacto['nombre'].capitalize()}")
                print(f"   Teléfono: {contacto['telefono']}")
                print(f"   Email: {contacto['email']}\n")
        else:
            print("📭 No se encontraron coincidencias.")
    
    elif opcion == 4:
        limpiar_terminal()
        print(f"\n--- EDITAR CONTACTO ---")

        buscar_nombre = input("Introduce parte del nombre del contacto a editar: ").lower()
        coincidencias = []

        for i, contacto in enumerate(contactos, start=1):
            if buscar_nombre in contacto["nombre"]:
                coincidencias.append((i, contacto))

        if not coincidencias:
            print("📭 No se encontraron coincidencias.")
        else:
            print("\nContactos encontrados:")
            for i, contacto in coincidencias:
                print(f"{i}. Nombre: {contacto['nombre'].capitalize()}")
                print(f"   Teléfono: {contacto['telefono']}")
                print(f"   Email: {contacto['email']}\n")

            try:
                seleccion = int(input("Indica el número del contacto que quieres editar: "))
                if 1 <= seleccion <= len(contactos):
                    nuevo_nombre = input("Introduce nuevo nombre (o pulsa Enter para mantener): ").strip().lower()
                    nuevo_telefono = input("Introduce nuevo teléfono (o pulsa Enter para mantener): ").strip()
                    nuevo_email = input("Introduce nuevo email (o pulsa Enter para mantener): ").strip().lower()

                    contacto = contactos[seleccion - 1]

                    if nuevo_nombre:
                        contacto["nombre"] = nuevo_nombre
                    if nuevo_telefono:
                        contacto["telefono"] = nuevo_telefono
                    if nuevo_email:
                        contacto["email"] = nuevo_email

                    print(f"✅ Contacto actualizado correctamente.")
                else:
                    print("❌ Número fuera de rango.")
            except ValueError:
                print("❌ Entrada inválida.")

    elif opcion == 5:
        limpiar_terminal()
        print(f"\n--- ELIMINAR CONTACTO ---")

        buscar_nombre = input("Introduce parte del nombre a buscar: ").lower()
        encontrados = []

        for i, contacto in enumerate(contactos, start=1):
            if buscar_nombre in contacto["nombre"]:
                encontrados.append((i, contacto))

        if not encontrados:
            print("📭 No se encontraron coincidencias.")
        else:
            print("\nContactos encontrados:")
            for i, contacto in encontrados:
                print(f"{i}. Nombre: {contacto['nombre'].capitalize()}")
                print(f"   Teléfono: {contacto['telefono']}")
                print(f"   Email: {contacto['email']}\n")

            try:
                seleccion = int(input("Indica el número del contacto que deseas eliminar: "))
                if 1 <= seleccion <= len(contactos):
                    eliminado = contactos.pop(seleccion - 1)
                    print(f"✅ Contacto '{eliminado['nombre']}' eliminado correctamente.")
                else:
                    print("❌ Número fuera de rango.")
            except ValueError:
                print("❌ Entrada inválida.")

    if opcion == 8:
        limpiar_terminal()
        print(f"¡Gracias por usar nuestra aplicación! Hasta pronto. 😊")
        break
    
    else:
        print("❌ Opción no válida. Por favor, selecciona un número del 1 al 8")

