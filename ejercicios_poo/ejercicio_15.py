# Define la clase Empleado que contiene dos atributos, nombre y edad empleado.
# La clase debe contener el constructor y los siguientes métodos:
# __del__: Un destructor que permite eliminar todas las referenrecias de un objeto.Este método especial
# también debe mostrar una cadenad e caracteres en la consola.

class Empleado:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad
        print(f"Empleado llamado {self.nombre} y de {self.edad} ha sido creado")

    def __del__(self):
        print(f"El destructor ha sido llamado, el empleado llamado {self.nombre} ha sido eliminado")

if __name__ == "__main__":
    
    empleado_1 = Empleado("Martin", 26)
    empleado_2 = Empleado("Julien", 24)
