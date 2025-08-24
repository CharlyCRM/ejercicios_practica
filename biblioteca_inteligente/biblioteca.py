
from __future__ import annotations
from libro import Libro
from usuario import Usuario
from typing import List

class Biblioteca:
    def __init__(self, usuarios_registrados:List=None, catalogo_libros:List=None, ): 
        self.catalogo_libros = catalogo_libros
        self.usuarios_registrados = usuarios_registrados

    def agregar_libro(self, libro:Libro) -> None:
        """Agrego un libro a la biblioteca"""
        self.catalogo_libros.append(libro)
        print(f"📙 Libro agregado a la Biblioteca")
        print("-" * 15)
        print(libro)

    def registrar_usuario(self, usuario:Usuario) -> None:
        """Agrega un usuaio al registro"""
        self.usuarios_registrados.append(usuario)
        print(f"👥 Usuario agregado al Registro")
