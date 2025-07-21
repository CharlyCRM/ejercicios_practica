# Define una clase Operación que tenga dos atributos: Dos números entreros x e y
# Esta clase nos permitirá realizar operaciones aritméticas entre estos dos atributos
# La clase debe tener constructor y los siguientes métodos
# suma: Un método  que permite realiza la suma entre los atrobutos
# multiplicación: Un método que permite realizar la multiplización entre los atributos
# división: Un método que permite realizar una división. SI el valor de y es igual a 0, este método debe retornar la frase:
# ¡División de x por y es imposible!

class Operacion:
    '''
    Clase para realizar Operaciones Aritméticas
        ARGS:
        x: número entero
        y: número entero
    '''
    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y
    
    def suma(self) -> int:
        resultado = self.x + self.y
        print(f"El resultado de sumar {self.x} + {self.y} = {resultado}")
    
    def multiplicaciones(self) -> int:
        resultado = self.x * self.y
        print(f"El resultado de multiplicaciones {self.x} * {self.y} = {resultado}")
    
    def division(self) -> int:
        try:
            resultado = self.x / self.y
            print(f"El resultado de dividir {self.x} / {self.y} = {resultado}")
        except Exception as e:
            print("!División de x por y es imposible!")

if __name__=="__main__":

    ope1 = Operacion(4,0)
    ope1.suma()
    ope1.multiplicaciones()
    ope1.division()