# Definir una clase Galleta que tenga dos atributos:
# Nombre de la galleta y su Forma
# La clase Galleta debe contener el constructor y el método hórnear que muestre dos frases

class Galleta:
    '''
    Generador de Galletas
    Args:
        Nombre: Nombre del objeto
        Forma: Forma del objeto
        Horno: Indica si la galleta esta dentro del horno
    '''
    def __init__(self, nombre:str, forma:str) -> print:
        self.nombre = nombre
        self.forma = forma
        self.horno = True
        
        print("Los atributos de su galleta se han generado correctamente")

    def hornear(self):
        '''
        Hornea la Galleta
        '''
        if self.horno:
            print(f"La galleta {self.nombre} de forma {self.forma} se está horneando")
        else:
            print(f"La galleta {self.nombre} de forma {self.forma} no está en el horno")



if __name__=="__main__":
    
    cookies = Galleta("cookies", "redonda")
    cookies.horno = False # cambio el valor del atributo
    cookies.hornear()