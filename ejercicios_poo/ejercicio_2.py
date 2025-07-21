# Definir una clase Libro que tenga tres atributos:
# Titulo del libro.
# Nombre del autor.
# Precio del libro.
# La clase libro debe contener el contrsutctor y el método informaciones que muestra la informacion relacionada con el libro

class Libro:
    '''
    Generador de Libros
    Args:
        Título: Tiíulo de la obra
        Nombre: FNombre del autor
        Precio: Precio en euros del producto
    '''
    def __init__(self, titulo:str, nombre:str, precio:int) -> None:
        self.titulo = titulo
        self.nombre = nombre
        self.precio = precio

    def mostrar_informaciones(self):
        print(f"El libro titulado '{self.titulo}', escrito por el autor/ar '{self.nombre}', se vende a un precio de {self.precio}€")

if __name__=="__main__":

    libro_1 = Libro("100 leguas de viaje submarino", "Julio Verne", 40)
    libro_1.mostrar_informaciones()