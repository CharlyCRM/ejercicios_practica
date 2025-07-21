# Definir una clase Ciruclo que tenga tres atributos:
# El radio y la posición de su centro con las variables (x, y)
# La clase contendrá su contructor y los siguientes métodos:
# area: Un método que permite calcular el área de un círculo
# perímetro: un método que permite calcular el perímetro de un círculo
# mostrar_propiedades: un método que permite mostrar las propiedades de un círculo, es decir, las coordenas de su centro y radio en cm

class Circulo:

    PI = 3.14
    '''
    Generador de la forma geométrica círculo
    ARGS:
        Radio: Radio del circulo en cm
        Posición: Posición de su centro definida en las coordenadas (x, y)
    '''
    def __init__(self, radio: float, x:float, y:float) -> None:
        self.radio = radio
        self.x = x
        self.y = y

    def area(self) -> float:
        '''
        Calcula el área de un circulo
        PI * (radio ** 2)
        '''
        # area = pow(self.radio,2) * PI
        area = self.PI * (self.radio ** 2)
        return area
    
    def perimetro(self) -> float:
        '''
        Calcula el perimetro del círculo
        2 * PI * radio
        '''
        perimetro = (2 * self.PI) * self.radio
        return perimetro

    def mostrar_propiedades(self) -> None:
        '''
        Muestra las propiedades del circulo y ejecuta los métodos anteriores
        '''
        print(f""""\n-- Propiedades del Círculo  --
        Centro: ({self.x}, {self.y})
        Radio: {self.radio} cm
        Area: {self.area()} cm
        Perimetro: {self.perimetro()} cm""")

        
    
if __name__== "__main__":
    
    cirulo_1 = Circulo(4, 2, 5)
    cirulo_1.mostrar_propiedades()
    
    print(50*"-")
    
    cirulo_2 = Circulo(7, 3, 10)
    cirulo_2.mostrar_propiedades()