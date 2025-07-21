# Definir la clase Persona con los siguientes atributos:
# Nombre: Nombre de la persona
# Edad: Edad de la persona
# género: Género de la persona
# La clase debe contener los siguiente métodos:
# Presentación: Un método que retorna una cadena de caracteres con la información de la persona
# esAdulto: Un método que verifica si una persona es adeulta, es decir si su edad es igual o mayor a 18 años
# El método retornar True si es adulto o False si no lo es

class Persona:
    '''
    Generador de personas
    ARGS:
        Nombre: Nombre de la persona
        Edad: Edad de la persona
        Género: Género de la persona
    '''
    def __init__(self, nombre:str, edad:int, genero:str) -> None:
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
    
    def presentacion(self) -> str:
        print(f" Mi nombre es {self.nombre}, tengo {self.edad}, y soy un {self.genero}")

    def esAdulto(self) -> bool:
        if self.edad >= 18:
            print("True")
            return True
        else:
            print("False")
            return False

if __name__== "__main__":

    alum_1 = Persona("Carlos", 35, "hombre")
    alum_1.presentacion()
    alum_1.esAdulto()

