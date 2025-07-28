# Clase Libro

class Libro:
    def __init__(self, titulo:str, autor:str, isbn:int, año:int, genero:str, disponible:bool):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.año = año
        self.genero = genero
        self.disponible = disponible

    def marcar_como_prestado(self) -> None:
        self.disponible = False
        print(f"📙 {self.titulo} ha sido prestado correctamente")

    def marcar_como_disponible(self) -> None:
        self.disponible = True
        print(f"📙 {self.titulo} ha sido devuelto correctamente")

    def __str__(self):
        return (
            f"Título: {self.titulo}"
            f"Autor: {self.autor}"
            f"ISBN: {self.isbn}"
            f"Año: {self.año}"
            f"Género: {self.genero}"
            f"Disponibilidad: {self.disponible}\n"
    )