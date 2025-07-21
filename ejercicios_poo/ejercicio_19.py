# Crea una clase principal llamada Texto que contenga un atributo llamado frase.
# Crea una clase hija llamada Textoltalico que herede de la clase Texto y contiene un
# único atributo llamado frase.
# Crea una segunda clase hija llmada TextoNegrita que hereda de la clase Texto y contiene
# un único atributo llamado frase.
# Las tres clases contienen un método mostras_texto(self) que se definirá de maneta diferentes
# según la clase a la que pertenece.

class Texto:
    
    def __init__(self, frase:str):
        self.frase = frase

    def mostrar_texto(self) -> str:
        print(f"{self.frase}")

class TextoItalico(Texto):
    
    def __init__(self, frase:str):
        super().__init__(frase)

    def mostrar_texto(self) -> str:
        print(f"_{self.frase}_")

class TextoNegrita(Texto):
    
    def __init__(self, frase:str):
        super().__init__(frase)

    def mostrar_texto(self):
        print(f"**{self.frase}**")

if __name__ == "__main__":

    # Creación de la instancia
    texto_1 = Texto("Aprender POO en Python a través de la práctica")
    texto_2 = TextoItalico("Aprender POO en Python a través de la práctica")
    texto_3 = TextoNegrita("Aprender POO en Python a través de la práctica")

    # Llamada al método
    texto_1.mostrar_texto()
    texto_2.mostrar_texto()
    texto_3.mostrar_texto()

