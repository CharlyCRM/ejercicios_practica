# Definir una clase MiCadenaPersonal que contenga un atributo: una cadena de caracteres
# La clase deve tener un constructor y los siguientes métodos especiales:
# __add__, __mul__, __len__, __str__, __contains__


class MiCadenaPersonal:

    def __init__(self, variable_str: str):
        self.variable_str = variable_str

    def __add__(self, cadena: str) -> str:
        """
        Concadena dos cadenas usando el caracter '|'
        """
        return f"La concatenación de candenas es: -- {self.variable_str} | {cadena.variable_str} --"

    def __mul__(self, valor: int):
        """
        Repite una cadena la cantidad de veces igual al valor indicado
        """
        # solución 1
        for i in range(valor):
            print(self.variable_str)

        # solución 2
        # return self.variable_str * valor

    def __len__(self) -> int:
        """
        Cuenta el número de caracteres exepto los incluidos en la lista
        """
        caracteres_eliminar = [",", "?", " ", "!", ".", "¡", "¿"]
        variable_sin_caracteres = self.variable_str

        for c in caracteres_eliminar:
            variable_sin_caracteres = variable_sin_caracteres.replace(c,"")
        
        return len(variable_sin_caracteres)
    
    def __str__(self):
        """
        Muestra el contenido de la cadea
        """
        return f"La cadena contiene el valor: {self.variable_str}"
    
    def __contains__(self, subcadena:str):
        """
        Comprueba si la cadena está contenida en el objeto de la clase
        """

        return subcadena in self.variable_str


if __name__ == "__main__":

    # __add__
    cadena_1 = MiCadenaPersonal("¡Hola!, ¿cómo estás?")
    cadena_2 = MiCadenaPersonal("Bienvenido a este curso")
    print(cadena_1 + cadena_2)
    
    # __nul__
    print("-" * 50)
    cadena_1 * 5

    # __len__
    print("-" * 50)
    print(len(cadena_2))

    # __str__
    print("-" * 50)
    print(cadena_2)

    # __contains__
    print("-" * 50)
    print("curso" in cadena_2)
    print("curso" in cadena_1)


