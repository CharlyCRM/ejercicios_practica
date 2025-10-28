# Clase de Ingrediente y Receta

from typing import Dict

from excepciones import RecetaInviable


class Ingrediente:
    def __init__(self, id: str, nombre: str, unidad: str, descripcion: str = None):
        self.id = id
        self.nombre = nombre
        # 'g', 'ml', 'unidad'
        self.unidad = unidad
        self.descripcion = descripcion

    def __str__(self):
        return (
            f"-- INGREDIENTE --\n"
            f"🔪 Id: {self.id}\n"
            f"🔪 Nombre: {self.nombre}\n"
            f"🔪 Unidad: {self.unidad}\n"
            f"🔪 Descripción: {self.descripcion}\n"
        )


class Receta:
    def __init__(
        self,
        id: str,
        nombre: str,
        tiempo_preparacion_min: int,
        ingredientes: Dict[str, float],
        categoria: str = None,
    ):
        self.id = id
        self.nombre = nombre
        self.tiempo_preparacion_min = tiempo_preparacion_min
        self.ingredientes = {} if ingredientes is None else ingredientes.copy()
        self.categoria = categoria

    def validar(self) -> None:
        """
        Casos de validación
        ---------------------
        - Cada receta tenga al menos un ingrediente.
        - Las cantidades de los ingredientes sean estrictamente positivas.
        - El tiempo de preparación (tiempo_preparacion_min) sea un entero positivo (no bool).
        - El identificador y el nombre no estén vacíos.
        """
        # id y nombre no vacíos tras strip()
        if not self.id or self.id.strip() == "" or not self.nombre or self.nombre.strip() == "":
            raise RecetaInviable("id y nombre no pueden estar vacíos")

        # tiempo de preparación: entero positivo (excluir bool)
        if not (isinstance(self.tiempo_preparacion_min, int)
                and not isinstance(self.tiempo_preparacion_min, bool)
                and self.tiempo_preparacion_min > 0):
            raise RecetaInviable("El tiempo de preparación debe ser un entero positivo")

        # ingredientes: diccionario no vacío
        if not isinstance(self.ingredientes, dict) or len(self.ingredientes) == 0:
            raise RecetaInviable("La receta debe tener al menos un ingrediente")

        # validar cada par (ingrediente, cantidad)
        for ingrediente, cantidad in self.ingredientes.items():
            # clave válida (defensa extra)
            if not isinstance(ingrediente, str) or ingrediente.strip() == "":
                raise RecetaInviable("El id del ingrediente debe ser una cadena no vacía")

            # primero: tipo numérico y no bool
            if not (isinstance(cantidad, (int, float)) and not isinstance(cantidad, bool)):
                raise RecetaInviable(f"La cantidad de '{ingrediente}' debe ser numérica (int/float)")

            # después: valor > 0
            if cantidad <= 0:
                raise RecetaInviable(f"La cantidad de '{ingrediente}' debe ser > 0")
                


