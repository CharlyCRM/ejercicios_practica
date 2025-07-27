# EJERCICIO: SIMULADOR DE COMBATE DE HÉROES Y MONSTRUOS

# Objetivo:
# Diseñar un juego de combate por turnos entre un héroe y un monstruo. 
# El sistema debe incluir estadísticas, tiradas de dados, gestión de vida, objetos curativos y habilidades especiales.

# Estructura del programa:

# 1. Clase Personaje (clase base):
#    - Atributos: nombre, clase, vida, dado de ataque, defensa.
#    - Métodos: lanzar_dado(), atacar(objetivo), esta_vivo(), __str__().
#
# 2. Clase Heroe (hereda de Personaje):
#    - Determina su dado de ataque según la clase (guerrero, pícaro, mago).
#    - Atributo adicional: pociones.
#    - Método usar_pocion(): lanza un dado de 20 caras para curar vida, sin superar la vida máxima.
#
# 3. Clase Monstruo (hereda de Personaje):
#    - Tiene frases aleatorias con grito_de_guerra().
#    - Aumenta su dado de ataque cada 5 rondas mediante aumentar_furia().
#
# 4. Clase Combate:
#    - Controla los turnos entre héroe y monstruo.
#    - Ofrece al jugador la opción de atacar o usar poción.
#    - Muestra el estado actual de vida y furia.
#    - Limpia la terminal y gestiona la presentación visual del combate.

import random
import os

class Personaje:
    def __init__(self, nombre:str, clase:str, vida:int, dado_ataque:int, defensa:int):
        self.nombre = nombre
        self.clase = clase
        self.vida = vida
        self.dado_ataque = dado_ataque
        self.defensa = defensa
        self.vida_maxima = vida

    def lanzar_dado(self):
        "Metodo que lanza un dado y define el valor de ataque"
        # obtener el numero de cara segun su clase
        caras = self.dado_ataque
        return random.randint(1, caras), caras

    def atacar(self, objetivo) -> None:
        "Reduce la vida en función de la defensa y el ataque recibido"
        ataque, caras = self.lanzar_dado()
        danio = max(ataque - objetivo.defensa, 0)
        objetivo.vida -= danio
        print(f"{self.nombre} ({self.clase.capitalize()}) lanza un dado de {caras} caras...")
        print(f"{self.nombre} ataca con un valor de ⚔️ {ataque}")
        print(f"{objetivo.nombre} se defiende con un valor de 🛡️ {objetivo.defensa}")
        print(f"💥 {self.nombre} ataca a {objetivo.nombre} y causa {danio} puntos de daño")
        print(f"❤️ {objetivo.nombre} tiene ahora {max(objetivo.vida, 0)} puntos de vida")

    def esta_vivo(self) -> bool:
        return self.vida > 0
    
    def __str__(self) -> str:
        return (
            f"🐾 Nombre: {self.nombre.capitalize()}\n"
            f"🔋 Tipo: {self.clase.capitalize()}\n"
            f"❤️ Vida: {self.vida}\n"
            f"⚔️ Ataque: {self.dado_ataque}\n"
            f"🛡️ Defensa: {self.defensa}"
        )
    
class Heroe(Personaje):
    def __init__(self, nombre, clase, vida, defensa, pociones):
        # Diccionario que asocia la clase del personaje con el número de caras del dado de ataque
        dados_por_clase = {
            "guerrero": 10,
            "picaro": 6,
            "mago": 8
        }
        dado_ataque = dados_por_clase.get(clase, 6)

        super().__init__(nombre, clase, vida, dado_ataque, defensa)
        self.pociones = pociones

    def usar_pocion(self):
        "Resta una poción y restaura vida lanzando un dado de 20 caras"

        if self.pociones > 0:
            vida_anterior = self.vida
            self.pociones = self.pociones - 1
            
            # Lanzar dado de 20 caras para determinar curación
            curacion = random.randint(1, 20)
            self.vida = min(self.vida + curacion, self.vida_maxima)
            vida_curada = self.vida - vida_anterior
            
            print(f"🧪 {self.nombre} usa una poción y lanza un dado de curación d20...")
            print(f"🎲 Resultado del dado: {curacion} puntos de curación")
            
            if vida_curada < curacion:
                print(f"💚 {self.nombre} se cura {vida_curada} puntos (limitado por vida máxima)")
            else:
                print(f"💚 {self.nombre} se cura {vida_curada} puntos de vida")
                
            print(f"❤️ {self.nombre} tiene ahora {self.vida}/{self.vida_maxima} puntos de vida")
            print(f"🧪 Te quedan {self.pociones} pociones")
        else:
            print(f"🚫 No tienes pociones para gastar 🧪")

class Monstruo(Personaje):
    def __init__(self, nombre, vida, dado_ataque, defensa):
        super().__init__(nombre, "monstruo", vida, dado_ataque, defensa)
        self.dado_ataque_base = dado_ataque  # Guardamos el ataque base original
        self.aumento_furia = 0  # Contador de aumentos de furia

    def aumentar_furia(self):
        """Aumenta el ataque del monstruo por la furia creciente"""
        self.aumento_furia += 1
        self.dado_ataque += 2
        print(f"🔥 ¡{self.nombre} entra en FURIA CRECIENTE!")
        print(f"💪 Su dado de ataque aumenta de d{self.dado_ataque - 2} a d{self.dado_ataque}")
        print(f"😡 Nivel de furia: {self.aumento_furia}")

    def grito_de_guerra(self):
        frases = [
            "¡Te aplastaré como a un insecto!",
            "¡Rugiré sobre tus huesos!",
            "¡No escaparás de mi furia!",
            "¡He derrotado héroes más fuertes que tú!",
            "¡Tiemblan los cielos cuando yo ataco!",
            "¡Tu final está escrito en mis garras!",
            "¡La oscuridad me guía!",
            "¡Serás mi próxima comida!",
            "¡Mi fuerza es legendaria!",
            "¡Siente el poder del abismo!"
        ]
        
        # Frases especiales cuando está furioso
        if self.aumento_furia > 0:
            frases_furia = [
                "¡MI FURIA NO CONOCE LÍMITES!",
                "¡CADA SEGUNDO ME VUELVO MÁS FUERTE!",
                "¡SIENTE EL PODER DE MI IRA CRECIENTE!",
                "¡LA SANGRE HIERVE EN MIS VENAS!",
                "¡MIS GOLPES SERÁN TU PERDICIÓN!"
            ]
            frases.extend(frases_furia)
        
        grito = random.choice(frases)
        print(f"🗣️ {self.nombre} grita: '{grito}'")

class Combate:
    def __init__(self, heroe: Heroe, monstruo: Monstruo):
        self.heroe = heroe
        self.monstruo = monstruo
    
    def limpiar_terminal(self):
        """Limpia la terminal para una mejor presentación visual"""
        # Detecta el sistema operativo y usa el comando apropiado
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def mostrar_estado(self):
        "Muestra el estado actual de vida de ambos personajes"
        print(f"\n📊 ESTADO ACTUAL:")
        print(f"🦸 {self.heroe.nombre}: {self.heroe.vida}/{self.heroe.vida_maxima} ❤️  |  🧪 Pociones: {self.heroe.pociones}")
        furia_texto = f" | 😡 Furia: +{self.monstruo.aumento_furia * 2}" if self.monstruo.aumento_furia > 0 else ""
        print(f"👹 {self.monstruo.nombre}: {self.monstruo.vida}/{self.monstruo.vida_maxima} ❤️  |  ⚔️ d{self.monstruo.dado_ataque}{furia_texto}")

    def iniciar_combate(self):
        "Turnos alternos de ataque hasta que uno quede con 0 vida"

        # Limpiar terminal para mejor presentación
        self.limpiar_terminal()

        print(f"\n🏟️ ==================== INICIAR COMBATE ====================")
        print(f"                    {self.heroe.nombre} ⚔️ VS ⚔️ {self.monstruo.nombre}")
        print(f"🏟️ ========================================================")
        
        # Mostrar estadísticas iniciales
        print(f"\n⚔️ ESTADÍSTICAS INICIALES:")
        print(f"🦸 {self.heroe.nombre} ({self.heroe.clase.capitalize()}): {self.heroe.vida} ❤️ | ⚔️ Dado d{self.heroe.dado_ataque} | 🛡️ {self.heroe.defensa} | 🧪 {self.heroe.pociones} pociones")
        print(f"👹 {self.monstruo.nombre} ({self.monstruo.clase.capitalize()}): {self.monstruo.vida} ❤️ | ⚔️ Dado d{self.monstruo.dado_ataque} | 🛡️ {self.monstruo.defensa}")
        print(f"⚠️ ALERTA: El monstruo aumentará su ataque en +2 cada 5 rondas (Furia Creciente)")

        contador_rounds = 1

        while self.heroe.esta_vivo() and self.monstruo.esta_vivo():
            print(f"\n--- ROUND {contador_rounds} ---")
            self.mostrar_estado()

            if contador_rounds % 2 != 0:  # Turno del héroe
                print(f"\n🗡️ Es el turno de {self.heroe.nombre}")
                
                # Sugerencia si la vida está baja (menos del 30%)
                if self.heroe.vida < self.heroe.vida_maxima * 0.3:
                    print("⚠️ ¡Tu vida está baja! Considera usar una poción.")
                
                # Validación de entrada mejorada
                accion_valida = False
                while not accion_valida:
                    accion = input(f"\n¿Quieres ATACAR (1) o usar POCIÓN (0)?\n").strip()
                    
                    if accion == "1":
                        self.heroe.atacar(self.monstruo)
                        accion_valida = True
                    elif accion == "0":
                        self.heroe.usar_pocion()
                        accion_valida = True
                    else:
                        print("❌ Opción inválida. Por favor ingresa 1 para atacar o 0 para usar poción.")
            
            else:  # Turno del monstruo
                print(f"\n👹 Es el turno de {self.monstruo.nombre}")
                self.monstruo.grito_de_guerra()
                self.monstruo.atacar(self.heroe)

            # Aumentar furia del monstruo cada 5 rondas
            if contador_rounds % 5 == 0 and self.monstruo.esta_vivo():
                print(f"\n{'='*50}")
                print(f"🔥 ¡ROUND {contador_rounds}! ¡EL MONSTRUO SE ENFURECE!")
                print(f"{'='*50}")
                self.monstruo.aumentar_furia()

            contador_rounds += 1

        # Después del bucle while
        print(f"\n🏟️ ==================== FIN DEL COMBATE ====================")
        self.mostrar_estado()
        
        if self.heroe.esta_vivo():
            print(f"\n🏆 ¡VICTORIA! {self.heroe.nombre} ha derrotado al monstruo {self.monstruo.nombre}!")
            print(f"🎉 El héroe sobrevive con {self.heroe.vida} puntos de vida y {self.heroe.pociones} pociones restantes.")
        else:
            print(f"\n💀 ¡DERROTA! El monstruo {self.monstruo.nombre} ha vencido al héroe {self.heroe.nombre}!")
            print(f"👹 El monstruo sobrevive con {self.monstruo.vida} puntos de vida.")
        
        print(f"⚔️ El combate duró {contador_rounds - 1} rounds.")
        if self.monstruo.aumento_furia > 0:
            print(f"😡 El monstruo alcanzó nivel de furia {self.monstruo.aumento_furia} (ataque final: d{self.monstruo.dado_ataque})")
        print(f"🏟️ ========================================================")

if __name__ == "__main__":
    # Heroes
    guerrero = Heroe(nombre="Arthas", clase="guerrero", vida=40, defensa=5, pociones=2)
    mago = Heroe(nombre="Merlin", clase="mago", vida=30, defensa=3, pociones=3)

    # Monstruos
    orco = Monstruo(nombre="Grommash", vida=35, dado_ataque=12, defensa=4)
    dragon = Monstruo(nombre="Azerath", vida=50, dado_ataque=20, defensa=6)

    combate = Combate(heroe=guerrero, monstruo=orco)
    combate.iniciar_combate()