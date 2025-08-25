from __future__ import annotations
from libro import Libro
from usuario import Usuario
from typing import List
from typing import Optional


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
        print("📙 Libro agregado a la Biblioteca")
        print("-" * 15)
        print(libro)

    def registrar_usuario(self, usuario: Usuario) -> None:
        """Agrega un usuario al registro"""
        self.usuarios_registrados.append(usuario)
        print("👥 Usuario agregado al Registro")

    def buscar_libro_por_titulo(self, titulo: str) -> List[Libro]:
        """Devuelve una lista de libros cuyo título contiene el texto dado (búsqueda case-insensitive)."""
        if not titulo:
            return []
        texto = titulo.lower()
        return [l for l in self.catalogo_libros if texto in l.titulo.lower()]

    def buscar_por_autor(self, autor: str) -> List[Libro]:
        """Devuelve una lista de libros cuyo autor contiene el texto dado (búsqueda case-insensitive)."""
        if not autor:
            return []
        texto = autor.lower()
        return [l for l in self.catalogo_libros if texto in l.autor.lower()]

    # --- Métodos auxiliares (internos) ---
    def _encontrar_usuario_por_id(self, usuario_id: int) -> Optional[Usuario]:
        for u in self.usuarios_registrados:
            if u.id == usuario_id:
                return u
        return None

    def _encontrar_libro_por_isbn(self, isbn: str | int) -> Optional[Libro]:
        for l in self.catalogo_libros:
            if str(l.isbn) == str(isbn):
                return l
        return None

    def prestar_libro_a_usuario(self, usuario_id: int, isbn: str | int) -> bool:
        """Presta un libro a un usuario por su ID y el ISBN del libro. Devuelve True si se prestó correctamente."""
        usuario = self._encontrar_usuario_por_id(usuario_id)
        if usuario is None:
            print("⚠️ Usuario no encontrado")
            return False

        libro = self._encontrar_libro_por_isbn(isbn)
        if libro is None:
            print("⚠️ Libro no encontrado en el catálogo")
            return False

        if not getattr(libro, "disponible", True):
            print("⚠️ El libro no está disponible")
            return False

        # Delegamos la lógica de reglas (máximo 3, etc.) al propio Usuario
        try:
            usuario.prestar_libro(libro)
            if hasattr(libro, "marcar_como_prestado"):
                libro.marcar_como_prestado()
            print("✅ Préstamo realizado")
            return True
        except Exception as e:
            # Por si el método del Usuario lanza alguna excepción de regla de negocio
            print(f"⚠️ No se pudo realizar el préstamo: {e}")
            return False

    def devolver_libro_de_usuario(self, usuario_id: int, isbn: str | int) -> bool:
        """Devuelve un libro prestado por un usuario. Devuelve True si la devolución fue correcta."""
        usuario = self._encontrar_usuario_por_id(usuario_id)
        if usuario is None:
            print("⚠️ Usuario no encontrado")
            return False

        libro = self._encontrar_libro_por_isbn(isbn)
        if libro is None:
            print("⚠️ Libro no encontrado en el catálogo")
            return False

        try:
            usuario.devolver_libro(libro)
            if hasattr(libro, "marcar_como_disponible"):
                libro.marcar_como_disponible()
            print("✅ Devolución realizada")
            return True
        except Exception as e:
            print(f"⚠️ No se pudo realizar la devolución: {e}")
            return False

    def mostrar_catalogo(self) -> None:
        """Imprime todo el catálogo de libros."""
        if not self.catalogo_libros:
            print("(Catálogo vacío)")
            return
        for libro in self.catalogo_libros:
            print(libro)

    def mostrar_libros_disponibles(self) -> None:
        """Imprime solo los libros disponibles."""
        disponibles = [l for l in self.catalogo_libros if getattr(l, "disponible", False)]
        if not disponibles:
            print("(No hay libros disponibles)")
            return
        for libro in disponibles:
            print(libro)
