# Crea una clase principal llmada TrabajadorEmpresa y dos clases hijas llamadas Director y Ingeniero.
# La clase TrabajadorEmpresa debe tener los siguientes atributos, nombre, salario y edad

class TrabajadorEmpresa:
    def __init__(self, nombre: str, salario:float, edad:int):
        self.nombre = nombre
        self.salario = salario
        self.edad = edad

    def mostrar_funcion(self) -> str:
        return f"Soy un trabajador de una empresa"

    def mostar_info(self):
        dict_datos = {}
        dict_datos["nombre"] = self.nombre
        dict_datos["salario"] = self.salario
        dict_datos["edad"] = self.edad

        return dict_datos

class Director(TrabajadorEmpresa):
    def __init__(self, nombre: str, salario:float, edad:int, prima:float):
        super().__init__(nombre, salario, edad)
        self.prima = prima

    def mostrar_funcion(self) -> str:
        return f"Soy un director de empresa"

    def mostrar_info(self):
        dict_datos = {}
        dict_datos["nombre"] = self.nombre
        dict_datos["salario"] = self.salario
        dict_datos["edad"] = self.edad
        dict_datos["prima"] = self.prima

        return dict_datos

class Ingeniero(TrabajadorEmpresa):
    def __init__(self, nombre: str, salario:float, edad:int):
        super().__init__(nombre, salario, edad)

    def mostrar_funcion(self) -> str:
        return f"Soy un ingeniero"

    def mostrar_info(self):
        dict_datos = {}
        dict_datos["nombre"] = self.nombre
        dict_datos["salario"] = self.salario
        dict_datos["edad"] = self.edad

        return dict_datos



if __name__ == "__main__":

    empleado1 = TrabajadorEmpresa("carlos", 1800, 35)
    print(empleado1.mostrar_funcion())
    print(empleado1.mostar_info())
    print("\n")

    director1 = Director("Alberto",3000, 56, 400)
    print(director1.mostrar_funcion())
    print(director1.mostrar_info())
    print("\n")

    ingeniero1 = Ingeniero("nombre", 2000, 34)
    print(ingeniero1.mostrar_funcion())
    print(ingeniero1.mostar_info())