# este ejercicio requiere el uso de la clase Persona del ejercicio 6
# Definir una clase Estudiante que herede de la clase Persona
# Esta clase debe tener el constructor y los siguientes métodos
# inscripción: Un método que toma como parámetros la lista de estudiantes inscritos y luego añade el nombre, la edad y el género del nuevo estudiante inscrito en la lista

from ejercicio_6 import Persona

class Estudiante(Persona):
    '''
    Generador de estudiantes que hereda de Persona
    '''
    def __init__(self, nombre: str, edad: int, genero: str) -> None:
        super().__init__(nombre, edad, genero)

    def inscripcion(self, lista:list) -> list:
        lista.append((self.nombre, self.edad, self.genero))
        print(f"Los estudiantes inscritos en los cursos son: {lista}")

if __name__ == "__main__":
    est1 = Estudiante ("Carlos", 34, "hombre")
    est2 = Estudiante ("Luis", 33, "hombre")
    est3 = Estudiante ("Maria", 30, "mujer")
    
    lista_estudiantes = []
    est1.inscripcion(lista_estudiantes)
    est2.inscripcion(lista_estudiantes)
    est3.inscripcion(lista_estudiantes)
