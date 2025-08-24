from __future__ import annotations
from libro import Libro
from usuario import Usuario
from typing import List


class Biblioteca:
    # Listas opcionales:
    # - Recibimos None por defecto y dentro del __init__ lo convertimos en [].
    # - ¿Por qué? Para NO usar listas mutables como valor por defecto (se compartirían entre instancias)
    #   y para garantizar que siempre tengamos una lista válida sobre la que hacer .append().
    def __init__(
        self,
        # Tipado: List[Usuario] y List[Libro] indican explícitamente qué contiene cada lista.
        usuarios_registrados: List[Usuario] | None = None,
        catalogo_libros: List[Libro] | None = None,
    ):
        self.catalogo_libros: List[Libro] = (
            catalogo_libros if catalogo_libros is not None else []
        )
        self.usuarios_registrados: List[Usuario] = (
            usuarios_registrados if usuarios_registrados is not None else []
        )

    def agregar_libro(self, libro: Libro) -> None:
        """Agrego un libro a la biblioteca"""
        self.catalogo_libros.append(libro)
        print(f"📙 Libro agregado a la Biblioteca")
        print("-" * 15)
        print(libro)

    def registrar_usuario(self, usuario: Usuario) -> None:
        """Agrega un usuario al registro"""
        self.usuarios_registrados.append(usuario)
        print(f"👥 Usuario agregado al Registro")
