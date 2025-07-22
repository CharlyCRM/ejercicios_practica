# ===========================================
# 💻 TIENDA INTERACTIVA EN PYTHON
# ===========================================

# Tareas a realizar:
# 1. Mostrar un menú con opciones hasta que el usuario decida salir.
# 2. Permitir al usuario:
#    - Ver el inventario con stock, precio y estado de caducidad.
#    - Vender productos si no están caducados y hay stock suficiente.
#    - Añadir nuevos productos al inventario (nombre, precio y stock).
#    - Marcar productos como caducados.
# 3. Usar bucle `while` para mantener el menú activo.
# 4. Usar `input()` para recibir instrucciones del usuario.

import os

def limpiar_terminal():
    os.system('cls' if os.name == 'nt'else 'clear')

inventario = {
    "manzanas": {"stock": 20, "precio": 0.5, "caducado": False},
    "leche": {"stock": 15, "precio": 1.1, "caducado": False},
    "pan": {"stock": 8, "precio": 0.8, "caducado": False},
    "huevos": {"stock": 30, "precio": 0.2, "caducado": False},
    "yogur": {"stock": 10, "precio": 0.9, "caducado": False},
    "galletas": {"stock": 5, "precio": 1.6, "caducado": False},
    "queso": {"stock": 4, "precio": 2.5, "caducado": False},
    "mantequilla": {"stock": 6, "precio": 1.9, "caducado": False}
}

while True:
    print("\n--- MENÚ TIENDA ---")
    print("1. Ver inventario")
    print("2. Vender producto")
    print("3. Añadir producto nuevo")
    print("4. Marcar producto como caducado")
    print("5. Salir")

    opcion = input("Selecciona una opción (1-5): ")

    if opcion == "1":
        limpiar_terminal()
        print("\n--- INVENTARIO ---")
        
        for producto, datos in inventario.items():
            print(f"Producto: {producto}")
            print(f"  Stock: {datos['stock']}")
            print(f"  Precio: {datos['precio']:.2f} €")
            print(f"  Caducado: {'Sí' if datos['caducado'] else 'No'}\n")

    elif opcion == "2":
        limpiar_terminal()
        print("\n--- INVENTARIO DE VENTAS ---")

        for producto, datos in inventario.items():
            print(f"Producto: {producto}")
            print(f"  Stock: {datos['stock']}\n")
        
        producto_venta = input("Indique el nombre del producto a vender: ").lower()

        if producto_venta in inventario:
            try:
                unidades_vendidas = int(input("Indique el número de unidades vendidas: "))
                limpiar_terminal()
                if not inventario[producto_venta]["caducado"] and inventario[producto_venta]["stock"] >= unidades_vendidas:
                    inventario[producto_venta]["stock"] -= unidades_vendidas
                    limpiar_terminal()
                    print(f"Venta realizada: {unidades_vendidas} unidades de {producto_venta}")
                else:
                    limpiar_terminal()
                    print("⚠️ No se puede realizar la venta: producto caducado o stock insuficiente.")
            except ValueError:
                limpiar_terminal()
                print("❌ Debes introducir un número entero.")
        else:
            limpiar_terminal()
            print("Ese producto no está en el inventario.")

    elif opcion == "3":
        limpiar_terminal()
        print(f"\n--- AGREGAR NUEVO PRODUCTO --- ")

        nuevo_producto = input("Introduzca el nombre del nuevo producto: ").lower()

        if nuevo_producto not in inventario:
            try:
                nuevo_producto_stock = int(input("Indique la cantidad de stock: "))
                nuevo_producto_precio = float(input("Indique el precio por unidad: "))
                
                inventario[nuevo_producto] = {
                    "stock": nuevo_producto_stock,
                    "precio": nuevo_producto_precio,
                    "caducado": False
                }

                limpiar_terminal()
                print(f"✅ Producto '{nuevo_producto}' agregado correctamente.")
                print(f"  Stock: {nuevo_producto_stock}")
                print(f"  Precio: {nuevo_producto_precio:.2f} €")
            except ValueError:
                print("❌ Error: debes introducir valores numéricos válidos.")
        else:
            print("⚠️ Ese producto ya existe en el inventario.")
    
    elif opcion == "4":
        limpiar_terminal()
        print(f"\n--- MARCAR PRODUCTO COMO CADUCADO ---")
        producto_caducado = input(f"Indique el nombre del producto").lower()

        if producto_caducado in inventario:
            inventario[producto_caducado]["caducado"] = True
            print(f"Estado cambio correctamente para {producto_caducado}")
        else:
            print(f"El prodcuto no existe en el inventario")
    

    elif opcion == "5":
        limpiar_terminal()
        print("¡Gracias por usar la tienda! Hasta pronto. 😊")
        break

    else:
        limpiar_terminal()
        print("Opción no válida. Por favor, selecciona un número del 1 al 5.")