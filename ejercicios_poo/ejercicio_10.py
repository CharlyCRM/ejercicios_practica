# Define una clase Empeladi con 4 atributos:
# Nombre del empleado
# Función
# Salario
# Número de horas trabajadas
# La clase Empleado debe contener el constructor y los métodos trabajar, info_sueldo, dar_aumento y info_funcion


class Empelado:
    """
    Generador de empleados
        ARGS de clase:
            horas_trabajadas: número de horas
        ARGS:
            Nombre: Nombre del empleado
            Función: Puesto del empleado
            Salario: Salario bruto mensual del empleado en euros
    """

    horas_trabajadas = 0

    def __init__(self, nombre: str, funcion: str, salario: float) -> None:
        self.nombre = nombre
        self.funcion = funcion
        self.salario = salario

    def trabajar(self, numero_horas: int) -> int:
        total_horas_trabajadas = self.horas_trabajadas + numero_horas
        print(f"El empleado {self.nombre} ha trabajado {total_horas_trabajadas} horas")
        return total_horas_trabajadas

    def info_sueldo(self) -> int:
        print(f"El empleado {self.nombre} recibe un salario de {self.salario}€")
        return {self.salario}

    def dar_aumento(self, cantidad: int) -> int:
        total_salario = self.salario + cantidad
        print(
            f"El empleado {self.nombre} ha recibido un aumento de {cantidad}, lo que le da un salario de {total_salario}€"
        )
        return total_salario

    def info_funcion(self) -> str:
        return f"El empelado {self.nombre} trabaja como {self.funcion}"


if __name__ == "__main__":

    empleado_1 = Empelado("Carlos", "Científico de Datos", 1500)
    empleado_1.trabajar(8)
    empleado_1.info_sueldo()
    empleado_1.dar_aumento(300)
    print(empleado_1.info_funcion())
