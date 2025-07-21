# Define la classe Calculo_Numerico que nos permita llevar a cabo varias operaciones numéricas. 
# Esta clase tiene un solo atributo, un número entero
# La clase calculo_numerico debe contener un constructor y los siguientes métodos: caluclo_factorial, lista_divisores, es Primo, esPar

class CalculoNumerico:
    '''
    Clase para realizar diferentes cálculos ariméticos
    '''

    def __init__(self, numero:float) -> None:
        self.numero = numero

    def calculo_factorial(self) -> int:
        if self.numero == 0:
            return 1
        else:
            resultado = 1
            for i in range (1, self.numero + 1):
                resultado *= i
            print(f"El factorial del número {self.numero} es: {resultado}")
            return resultado
        
    def lista_divisores(self) -> int:
        divisores = []
        for i in range(1, self.numero + 1):
            if self.numero % i == 0:
                divisores.append(i)
        return f"La lista de divisiones del número {self.numero} es: {divisores}"
    
    def es_primo(self) -> int:
        lista_dos_divisores = self.lista_divisores()

        if len(lista_dos_divisores) == 2:
            print(f"El número {self.numero} es primo")
        else:
            print(f"El numero {self.numero} no es primo")

    def es_par(self) -> int:
        if self.numero % 2 == 0:
            print(f"El número {self.numero} es par")
        else:
            print(f"El número {self.numero} es impart")
        
        
if __name__ == "__main__":

    calculo_1 = CalculoNumerico(14)
    calculo_1.calculo_factorial()
    print(calculo_1.lista_divisores())
    calculo_1.es_primo()
    calculo_1.es_par()
    