# Crea una clase llamada Animal, que tenga un único atributo llamado nombre del animal.
# Una clase hija llmada Gato que hereda de la clase Animal, con un único atributo, nombre del gato.
# Una segunda clase hija llmada Perro que hereda de la clase Animal con un único atributo, nombre del perro.
# las tres clases contienen un método hablar(self) que se definirá de manera diferente se´gun la clase a la que pertenece.

class Animal:
    def __init__(self, nombre: str):
        self.nombre = nombre

    def hablar(self) -> None:
        return None

class Gato(Animal):
    def __init__(self, nombre: str):
        super().__init__(nombre)
    
    def hablar(self) -> str:
        print(f"{self.nombre} dice ¡Miau miua!")

class Perro(Animal):
    def __init__(self, nombre:str):
        super().__init__(nombre)

    def hablar(self) -> str:
        print(f"{self.nombre} dice ¡Guau guau!")


if __name__ == "__main__":
    
    # Instancia de clase
    rocky = Perro("Rocky")
    felix = Gato("Felix")
    # Llamada al método
    rocky.hablar()
    felix.hablar()
