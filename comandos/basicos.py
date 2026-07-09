"""
===========================================
GRASSHOPPER AI
Comandos básicos
===========================================
"""

from datetime import datetime
from config import ASSISTANT_NAME

from comandos.capturas import captura_pantalla
from comandos.modos import modo_trabajo
from comandos.musica import reproducir_musica

from sistema.abrir import (
    abrir_google,
    abrir_chatgpt,
    abrir_youtube,
    abrir_vscode,
    abrir_terminal
)


def procesar_comando(comando, hablar, escuchar):

    comando = comando.lower()

    # -------------------------
    # SALIR
    # -------------------------

    if "salir" in comando:

        hablar("Hasta luego.")
        return True

    # -------------------------
    # SALUDOS
    # -------------------------

    elif any(palabra in comando for palabra in [
        "hola",
        "buenas",
        "hey"
    ]):

        hablar("Hola. ¿Qué necesitas?")

    # -------------------------
    # NOMBRE
    # -------------------------

    elif "nombre" in comando:

        hablar(f"Mi nombre es {ASSISTANT_NAME}.")

    # -------------------------
    # HORA
    # -------------------------

    elif "hora" in comando:

        hora = datetime.now().strftime("%H:%M")

        hablar(f"Son las {hora}")

    # -------------------------
    # FECHA
    # -------------------------

    elif "fecha" in comando:

        fecha = datetime.now().strftime("%d de %m de %Y")

        hablar(f"Hoy es {fecha}")

    # -------------------------
    # GOOGLE
    # -------------------------

    elif "abre google" in comando:

        abrir_google()

        hablar("Abriendo Google.")

    # -------------------------
    # CHATGPT
    # -------------------------

    elif (
        "abre chatgpt" in comando
        or "abre chat g p t" in comando
        or "abre chat gpt" in comando
    ):

        abrir_chatgpt()

        hablar("Abriendo ChatGPT.")

    # -------------------------
    # YOUTUBE
    # -------------------------

    elif "abre youtube" in comando:

        abrir_youtube()

        hablar("Abriendo YouTube.")

    # -------------------------
    # VS CODE
    # -------------------------

    elif (
        "abre visual studio code" in comando
        or "abre vscode" in comando
        or "abre vs code" in comando
    ):

        abrir_vscode()

        hablar("Abriendo Visual Studio Code.")

    # -------------------------
    # TERMINAL
    # -------------------------

    elif (
        "abre terminal" in comando
        or "abre powershell" in comando
    ):

        abrir_terminal()

        hablar("Abriendo la terminal.")

    # -------------------------
    # MODO TRABAJO
    # -------------------------

    elif "modo trabajo" in comando:

        modo_trabajo(hablar, escuchar)

    
    # -------------------------
    # CAPTURA DE PANTALLA
    # -------------------------

    elif (
        "captura de pantalla" in comando
        or "haz una captura" in comando
        or "haz una captura de pantalla" in comando
    ):

        ruta = captura_pantalla()

        hablar("Captura guardada correctamente.")

        print(f"Captura guardada en: {ruta}")

    # -------------------------
    # MÚSICA
    # -------------------------

    elif (
        "pon música" in comando
        or "pon musica" in comando
        or "reproduce" in comando
    ):

        respuesta = reproducir_musica(comando)

        hablar(respuesta)

    # -------------------------
    # ERROR
    # -------------------------

    else:

        hablar("No conozco ese comando.")

    return False