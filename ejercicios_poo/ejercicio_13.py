class Vector4D:
    """
    Una clase que representa un vector en 4 dimensiones con los atributos u, v, x e y.

    Atributos:
    -----------
    u : int
        Componente del vector en la primera dimensión.
    v : int
        Componente del vector en la segunda dimensión.
    x : int
        Componente del vector en la tercera dimensión.
    y : int
        Componente del vector en la cuarta dimensión.
    """

    def __init__(self, u: int, v: int, x: int, y: int) -> None:
        self.u = u
        self.v = v
        self.x = x
        self.y = y

    def __add__(self, vector) -> 'Vector4D':
        """
        Suma dos vectores 4D.

        Parámetros:
        -----------
        vector : Vector4D
            El vector a sumar con el vector actual.

        Devuelve:
        -----------
        Vector4D
            Un nuevo vector que es la suma del vector actual y el vector dado.
        """
        sumar = Vector4D(self.u + vector.u, self.v + vector.v, self.x + vector.x, self.y + vector.y)
        return sumar

    def __sub__(self, vector) -> 'Vector4D':
        """
        Resta dos vectores 4D.

        Parámetros:
        -----------
        vector : Vector4D
            El vector a restar del vector actual.

        Devuelve:
        -----------
        Vector4D
            Un nuevo vector que es la resta del vector actual y el vector dado.
        """
        restar = Vector4D(self.u - vector.u, self.v - vector.v, self.x - vector.x, self.y - vector.y)
        return restar

    def __mul__(self, vector) -> 'Vector4D':
        """
        Multiplica dos vectores 4D componente por componente.

        Parámetros:
        -----------
        vector : Vector4D
            El vector a multiplicar con el vector actual.

        Devuelve:
        -----------
        Vector4D
            Un nuevo vector que es el producto componente por componente del vector actual y el vector dado.
        """
        multiplicar = Vector4D(self.u * vector.u, self.v * vector.v, self.x * vector.x, self.y * vector.y)
        return multiplicar

    def __truediv__(self, vector) -> 'Vector4D':
        """
        Divide dos vectores 4D componente por componente.

        Parámetros:
        -----------
        vector : Vector4D
            El vector por el cual se divide el vector actual.

        Devuelve:
        -----------
        Vector4D
            Un nuevo vector que es el cociente componente por componente del vector actual y el vector dado.
        """
        dividir = Vector4D(self.u / vector.u, self.v / vector.v, self.x / vector.x, self.y / vector.y)
        return dividir

    def __repr__(self) -> str:
        """
        Representación en cadena del objeto Vector4D.

        Devuelve:
        -----------
        str
            Una cadena que representa el vector en el formato "Vector4D(u, v, x, y)".
        """
        return f"Vector4D({self.u}, {self.v}, {self.x}, {self.y})"


if __name__ == "__main__":
    vector_1 = Vector4D(2, 3, 4, 5)
    vector_2 = Vector4D(4, 1, 3, 6)
    
    suma = vector_1 + vector_2
    resta = vector_1 - vector_2
    division = vector_1 / vector_2
    multiplicacion = vector_1 * vector_2
    
    print(f"La suma de {vector_1} y {vector_2} es {suma}")
    print(f"La resta de {vector_1} y {vector_2} es {resta}")
    print(f"La división de {vector_1} y {vector_2} es {division}")
    print(f"La multiplicación de {vector_1} y {vector_2} es {multiplicacion}")