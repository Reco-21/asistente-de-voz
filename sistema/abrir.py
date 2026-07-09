
"""
===========================================
GRASSHOPPER AI
Sistema para abrir aplicaciones
===========================================
"""

import subprocess
import webbrowser
import os

# ====================================================
# CONFIGURA AQUÍ LAS RUTAS DE TUS PROGRAMAS
# ====================================================

# Cambia TU_USUARIO por tu nombre de usuario de Windows
VSCODE = r"C:\Users\gesu2\AppData\Local\Programs\Microsoft VS Code\Code.exe"

# PowerShell
POWERSHELL = "powershell"

def abrir_terminal():

    subprocess.Popen("powershell")
# ====================================================
# PÁGINAS WEB
# ====================================================

CHATGPT = "https://chatgpt.com"

GOOGLE = "https://www.google.com"

YOUTUBE = "https://www.youtube.com"

YOUTUBE_MUSIC = "https://music.youtube.com"

GITHUB = "https://github.com"


# ====================================================
# FUNCIONES
# ====================================================

def abrir_vscode():

    if os.path.exists(VSCODE):
        subprocess.Popen(VSCODE)
        return True

    return False


def abrir_powershell():

    subprocess.Popen(POWERSHELL)


def abrir_chatgpt():

    webbrowser.open(CHATGPT)


def abrir_google():

    webbrowser.open(GOOGLE)


def abrir_youtube():

    webbrowser.open(YOUTUBE)


def abrir_youtube_music():

    webbrowser.open(YOUTUBE_MUSIC)


def abrir_github():

    webbrowser.open(GITHUB)