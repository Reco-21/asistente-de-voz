"""
===========================================
GRASSHOPPER AI
Organizador de ventanas
===========================================
"""

import time
import ctypes
import pygetwindow as gw


def buscar(titulo):

    ventanas = gw.getWindowsWithTitle(titulo)

    if ventanas:
        return ventanas[0]

    return None


def organizar_modo_trabajo():

    # Esperamos unos segundos para que se abran
    time.sleep(4)

    user32 = ctypes.windll.user32

    ancho = user32.GetSystemMetrics(0)
    alto = user32.GetSystemMetrics(1)

    # -------------------------
    # VS CODE
    # -------------------------

    vscode = buscar("Visual Studio Code")

    if vscode:

        vscode.restore()

        vscode.moveTo(0, 0)

        vscode.resizeTo(
            int(ancho * 0.65),
            alto
        )

    # -------------------------
    # CHATGPT
    # -------------------------

    chatgpt = buscar("ChatGPT")

    if chatgpt:

        chatgpt.restore()

        chatgpt.moveTo(
            int(ancho * 0.65),
            0
        )

        chatgpt.resizeTo(
            int(ancho * 0.35),
            int(alto * 0.55)
        )

    # -------------------------
    # EXPLORADOR
    # -------------------------

    explorador = buscar("Explorador de archivos")

    if explorador is None:
        explorador = buscar("File Explorer")

    if explorador:

        explorador.restore()

        explorador.moveTo(
            int(ancho * 0.65),
            int(alto * 0.55)
        )

        explorador.resizeTo(
            int(ancho * 0.35),
            int(alto * 0.45)
        )