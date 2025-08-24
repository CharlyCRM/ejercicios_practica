# Clase usuario

# annotations -> Permite que las anotaciones de tipo (type hints) se almacenen como cadenas en vez de evaluarse al momento.
# Esto evita problemas con referencias adelantadas o circulares entre clases (ej. Usuario <-> Libro).
from __future__ import annotations
from libro import Libro
from typing import List
from datetime import datetime

class Usuario:
    def __init__(self, nombre:str, id:int, libros_prestados:List = None, historial_prestamos:List = None):
        self.nombre = nombre
        self.id = id
        self.libros_prestados = libros_prestados
        self.historial_prestamos = historial_prestamos

    def prestar_libro(self, libro:Libro):
        "Verifica si el libro está disponible y si es así le cambia el estado"
        if libro.disponible:
            libro.disponible = False
            self.libros_prestados.append(libro)
            self.historial_prestamos.append(libro)
            print(f"📚 {self.nombre} ha prestado el libro {libro.titulo}")
        else:
            print(f"❌ El libro {libro.titulo} no está disponible para prestamos")

    def devolver_libro(self, libro:Libro):
        "Confirma si el libro a sido prestado, y si es así, lo devuelve"
        if libro not in self.libros_prestados:
            print(f"⚠️ Este libro no ha sido prestado por ti")
            return
        else:
            self.libros_prestados.remove(libro)
            libro.disponible = True
            print(f"📙 {libro.titulo} ha sido devuelto correctamente")

    def mostrar_historial(self):
        "Muestra el historial de libros pestados"
        if len(self.historial_prestamos) <=0:
            print(f"🕵️ El usuario todavía no ha prestado ningún libro.")
        else:
            print(f"\n--- HISTORIAL PRÉSTAMOS DE {self.nombre} ---")
            for libro in self.historial_prestamos:
                print(f"Título: {libro.titulo}")
                print(f"Autor: {libro.autor}")
                print(f"ISBN: {libro.isbn}")
                print(f"Año: {libro.año}")
                print(f"Género: {libro.genero}")
                print(f"Disponibilidad: {libro.disponible}\n")

    def bloquear_prestar(self, libro:Libro) -> None:
        DIAS_PRESTAMO_MAXIMO = 60
        dias_prestado = datetime.today - DIAS_PRESTAMO_MAXIMO

        if libro. > dias_prestado:
