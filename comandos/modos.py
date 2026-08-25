
import time
from sistema.proyectos import abrir_proyecto


import time

from sistema.proyectos import abrir_proyecto


def modo_trabajo(hablar, escuchar):

    MAX_INTENTOS = 2

    for intento in range(MAX_INTENTOS):

        hablar("¿Qué proyecto quieres abrir?")

        # Espera para que termine de hablar
        time.sleep(0.75)

        proyecto = escuchar.escuchar()

        if proyecto == "":
            hablar("No te he entendido.")
            continue

        correcto = abrir_proyecto(proyecto)

        if correcto:

            hablar(f"Abriendo el proyecto {proyecto}.")

            return

        else:

            hablar("Ese proyecto no existe.")

    hablar("No he podido abrir ningún proyecto.")


def modo_estudio(hablar):

    hablar("Modo estudio aún no está disponible.")


def modo_descanso(hablar):

    hablar("Modo descanso aún no está disponible.")