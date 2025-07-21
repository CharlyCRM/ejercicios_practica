# Define dos clases padres, la clase Video y la clase Audio. A continuación crea una subclase Media que herede de las clases Video y Audio.
# Atributos clase Vídeo: Titulo del video, duración en minutos y categ´roai del video
# Atributos de la clase Audio: Título del audio y nombre de artista
# Atributos de Media: Título del mesio, categória, duración y nombre del artista.
# Cada clase tiene su propio constructor y sus propios métodos:
# Clase Vídeo, mirar_video y detener_video
# Clase Audio: escuchar_audio y detener_audio
# Clase Media solo el constructor

class Video:
    '''
    Generador de Vídeos
        ARGS:
            Título: Título del vídeo
            Duración: Duración del vídeo en minutos
            Categoria: Categoria de la película
    '''
    def __init__(self, titulo:str, duracion:int, categoria:str) -> None:
        self. titulo = titulo
        self.duracion = duracion
        self.categoria = categoria

    def mirar_video(self) -> str:
        print(f"El vídeo que estás viendo se titula '{self.titulo}' de la categoría '{self.categoria}' con una duración de {self.duracion} minutos")

    def detener_video(self) -> str:
        print(f"Deteniendo la reproducción del vídeo....")

class Audio:
    '''
    Generador de Audio
        ARGS:
            Título: Título del audio
            Artista: Nombre del artista del audío
    '''
    def __init__(self, titulo:str, artista:str) -> None:
        self.titulo = titulo
        self.artista = artista

    def escuchar_audio(self) -> str:
        print(f"El audio que estás escuando es '{self.titulo}' producido por el/la artista '{self.artista}'")

    def detener_audio(self) -> str:
        print(f"Deteniendo la reproducción del audio....")

class Media(Video, Audio):
    '''
    Clase Media que hereda de Video y Audio
    ARGS:
        Título: Título del vídeo
        Duración: Duración del vídeo en minutos
        Categoria: Categoria de la película
        Artista: Nombre del artista del audío
    '''
    def __init__(self, titulo: str, duracion: int, categoria: str, artista:str) -> None:
        Video.__init__(self, titulo, duracion, categoria)
        Audio.__init__(self, titulo, artista)


if __name__ == "__main__":

    medio_1 = Media("El mago de Oz", 120, "Infantil", "Judy Garlan")
    medio_1.escuchar_audio()
    medio_1.mirar_video()
    medio_1.detener_audio()
    medio_1.detener_video()