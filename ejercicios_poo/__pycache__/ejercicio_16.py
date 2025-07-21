# Definir una clase ManipuladoresArchivos que contiene dos atributos: nombre del archivo (o path) y un atributo que
# contiene el objeto retornado después de abrir el archivo en modo lectura y escritura.
# la clase debe conteer un constructor, un destructor y el siguiente método:
# escribir_archivos(self, frase) Este método nos debe permitir escribir la frase pasada como parámetro en el archivo.
# También permite mostrar una cadena en al consola.


class ManipulardoresArchivos:

    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo
        self.archivo = open(nombre_archivo, "a")  # abre el fichero en modo append

        print(
            f"El archivo '{self.nombre_archivo}' ha sido abierto en modo lectura y escritura"
        )

    def __del__(self):
        if not self.archivo.closed:
            self.archivo.close()
        print(f"El archivo '{self.nombre_archivo}' ha sido cerrado.")

    def escribir_archivo(self, frase: str):
        """
        Escribe texto en un documento
        """
        self.archivo.write(frase + "\n")
        self.archivo.close
        print(f"la frase: '{frase}' ha sido incluida en el archivo '{self.nombre_archivo}'")


if __name__ == "__main__":

    archivo_1 = ManipulardoresArchivos("prueba_16.txt")
    archivo_1.escribir_archivo("Este texto lo he incluido a través del programa")
