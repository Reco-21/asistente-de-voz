"""
===========================================
GRASSHOPPER AI
Gestor de proyectos
===========================================
"""

import os
import subprocess
import webbrowser
from sistema.ventanas import organizar_modo_trabajo
from mis_proyectos import PROYECTOS
from sistema.abrir import VSCODE


def abrir_proyecto(nombre):

    nombre = nombre.lower().strip()

    if nombre not in PROYECTOS:
        return False

    ruta = PROYECTOS[nombre]

    if not os.path.exists(ruta):
        return False

    # VS Code
    subprocess.Popen([
    VSCODE,
    "--new-window",
    ruta
])

    # ChatGPT
    webbrowser.open("https://chatgpt.com")


    # Explorador
    subprocess.Popen([
        "explorer",
        ruta
    ])
    organizar_modo_trabajo()

    return True