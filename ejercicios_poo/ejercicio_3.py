# Definir la clase Notas que tenga dos atributos
# Nombre del estudiante
# Nota del estudiante
# La clase nota debe tener un método que permita verificar si un estudiante ha aprobado el examen.
# Si la nota del estudiante supera los 75 puntos, entonces el estudiante ha aprobado, de lo contraro a suspendido
# El metodo debe mostrar si el estudiante aprueba o suspende

class Notas():
    '''
    Clase para generar las nota del estudiante
    ARGS:
        Nombre: Nombre del estudiante
        Nota: Nota resultado del examen
    '''
    def __init__(self, nombre:str, nota: int) -> None:
        self.nombre = nombre
        self.nota = nota

    def ha_pasado(self):
        if self.nota >= 75:
            print(f"El alumno {self.nombre} ha superado el examen con un nota de {self.nota} sobre 100")
        else:
            print(f"El alumno {self.nombre} ha suspendido el examen con un nota de {self.nota} sobre 100")

if __name__=="__main__":
    alumno_1 = Notas("Pedro", 80)
    alumno_1.ha_pasado()
    print(50*"-")
    alumno_2 = Notas("Maria", 30)
    alumno_2.ha_pasado()