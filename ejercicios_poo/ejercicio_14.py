# Define una clase Carta que contenga dos atributos. El rango de la carta y su símbolo
# La clase carta debe contener el constructor y los siguientes métodos: __eq__, __it__, __str__
# __eq__(self, carta): Este método especial nos debe permitir verificar si dos cartas son iguales 
# comprobando si tienen el mismo rango y el mismo símbolo.
# __it__(self, carta): Este método especial nos permitirá compara las cartas según su rango y su símbolo.
#__str__(self, carta): Este método especial nos debe permitir personalizar la representación en cadena de caracteres de la carta.
# Por lo tanto, la cadena de caracteres devuelta debe contener el rango y el símbolo de la carta

class Carta:
    def __init__(self, rango:dict, simbolo:list) -> None:
        self.rango = rango
        self.simbolo = simbolo
        print(self.rango, self.simbolo)
        
    def __eq__(self, carta) -> None:
        if carta.rango == self.rango and carta.simbolo == self.simbolo:
            return f"Las Cartas son Iguales: {self.rango} {self.simbolo}"
        else:
            return f"Las Cartas son Diferentes: {carta.rango} {carta.simbolo}"
        
        
    def __lt__(self, carta) -> None:
        if self.rango == carta.rango:
            return self.simbolo < carta.simbolo
        return self.rango < carta.rango
        
    def __str__(self) -> None:
        return f"rango {self.rango} y símbolo {self.simbolo}"
        
        

if __name__ == "__main__":
    signos = [chr(9824), chr(9825), chr(9826), chr(9827)]
    rangos = {
        "2": 2, 
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 1
    }
    
    
    carta_1 = Carta(rangos["A"], signos[0])
    carta_2 = Carta(rangos["A"], signos[0])
    carta_3 = Carta(rangos["K"], signos[1])
    
    print(carta_1 == carta_2)
    print(carta_1 > carta_3)
    print(f"La carta_1 tiene {carta_1}")
        
    
    