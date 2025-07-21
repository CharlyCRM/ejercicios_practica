# Define una clase Dado con un atributo resultado que corresponde al resultado botenido despues de lanzar el dado
# La clase dao debe contener el contrusctor y los siguientes métodos
# lanzar_dado: Un método que permite lanzar el dado y obtener un resultado aleatorio entra 1 y 6
# mostrar_puntos: Un método que permite mistrar los puntos obtenidos tras el lanzamiento del dado

import random

class Dado:
    '''
    Clase que genera un Dado
    ARGS:
        Resultado: Resultado del lanzamiento del dado
    '''
    def __init__(self, resultado = None) -> None:
        self.resultado = resultado
    
    def lanzar_dado(self) -> int:
        '''
        Genera un resultado aleatorio comprendido entre el 1 y el 6
        '''
        self.resultado = random.randint(1, 6)
        return self.resultado
    
    def mostrar_puntos(self)-> int:
        '''
        Muestra el resultado del lanzamiento del dado
        '''
        print(f"El número de puntos obtenido es: {self.resultado}")
    
if __name__ == "__main__":
    
    tirada = Dado()
    tirada.lanzar_dado()
    tirada.mostrar_puntos()
