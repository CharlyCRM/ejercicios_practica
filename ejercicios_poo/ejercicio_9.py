# Definir una clase Vehiculo y una clase Coche que herede de la clase Vehiculo. La clase Vehiculo contiene 2 atributos:
# Marca del vehiculo y una velocidad incial con un valor prediterminado de 0.
# La sublcase Coche tiene un atributo adicional llamado bocina con un valor predeterminado = "¡tuuuuut!"
# La clase Vehiculo debe contener el contructor y los siguientes métodos:
# acelerar(selv,v) Un método que permite aumentar la velocidad actual del vehículo con una velocidad v pasada como parámetro
# desacelerar(self,v) un métodos que permite reducir la veloidad actual del cehículo con una velocidad v pasas como parámetro
# mostrar_velocidad: Este métdo muestra la velocidad actual del vechículo
# La subclase coche de contener el constructo y un mñetodo adicional.
# tocar_clazon(self) .Este método sirve par tocar la bocina mostrnado una cadena de caracteres

class Vehiculo:
    '''
    Crea la clase vehículo
    ARGS:
        Marca: Marca del vehículo
        Velocidad: Velocidad inicial del vehículo
    '''
    def __init__(self, marca:str, velocidad:int = 0) -> None:
        self.marca = marca
        self.velocidad = int(velocidad)
        print(f"La velocidad actual del coche es {self.velocidad}")
    
    def acelerar(self, v:int) -> int:
        '''
        Increment a la velocidad el vehículo en función del valor de v
        '''
        self.velocidad += v
        print(f"La velocidad ha sido incrementada en {self.velocidad}")
        return self.velocidad
    
    def desacelerar(self, v:int) -> int:
        '''
        Reduce la velocidad el vehículo en función del valor de v
        '''
        self.velocidad -= v
        print(f"La velocidad ha sido reducida en {self.velocidad}")
        return self.velocidad
    
    def mostrar_velocidad(self) -> None:
        '''
        Muestra la velocidad actual
        '''
        print(f"la velocidad actual es {self.velocidad}")

class Coche(Vehiculo):
    '''
    Crea la clase Coche que Hereda de Vechículo
    ARGS:
        Marca: Marca del vehículo
        Velocidad: Velocidad inicial del vehículo
        bocina: Sonido que realiza el vehículo al tocar el claxón
    '''
    def __init__(self, marca: str, velocidad = 0, bocina = "¡tuuuuuu!") -> None:
        super().__init__(marca, velocidad)
        self.bocina = bocina

    def tocar_claxon(self) -> None:
        '''
        Imprime por pantalla el sonido que realiza el vehículo
        '''
        print(self.bocina)


if __name__ == "__main__":

    coche_1 = Coche("Ford", " 50")
    coche_1.acelerar(30)
    coche_1.desacelerar(10)
    coche_1.tocar_claxon()