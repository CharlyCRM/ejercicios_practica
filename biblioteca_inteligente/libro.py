# Clase Libro
from datetime import date

class Libro:
    def __init__(self, titulo:str, autor:str, isbn:int, año:date, genero:str, disponible:bool):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.año = año
        self.genero = genero
        self.disponible = disponible

    def marcar_como_prestado(self) -> None:
        """Marca un libro como prestado cambiando el atributo dispinible a false"""
        self.disponible = False
        print(f"📙 {self.titulo} ha sido prestado correctamente")

    def marcar_como_disponible(self) -> None:
        """Marca un libro como disponible cambiando el atributo dispinible a true"""
        self.disponible = True
        print(f"📙 {self.titulo} ha sido devuelto correctamente")

    def __str__(self):
        return (
            f"Título: {self.titulo}\n"
            f"Autor: {self.autor}\n"
            f"ISBN: {self.isbn}\n"
            f"Año: {self.año}\n"
            f"Género: {self.genero}\n"
            f"Disponibilidad: {self.disponible}\n"
    )

    def es_nuevo(self) -> None:
        """Comprueba si el libro es nuevo (< 2 años)"""
        if self.año < date.today():
            print(f"📙 {self.titulo} es un libro antígüo")
        else:
            print(f"📙 {self.titulo} es un libro nuevo")
