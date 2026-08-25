

from config import YOUTUBE_MUSIC_LOAD_TIME, YOUTUBE_MUSIC_TABS
import time
import urllib.parse
import webbrowser

import keyboard


def reproducir_musica(comando):

    comando = comando.lower()

    # Limpiar el comando
    for texto in [
        "pon música de",
        "pon musica de",
        "pon música",
        "pon musica",
        "reproduce"
    ]:
        comando = comando.replace(texto, "")

    busqueda = comando.strip()

    if not busqueda:
        return "¿Qué quieres escuchar?"

    url = (
        "https://music.youtube.com/search?q="
        + urllib.parse.quote(busqueda)
    )

    webbrowser.open_new_tab(url)

    # Esperar a que cargue Edge
    time.sleep(YOUTUBE_MUSIC_LOAD_TIME)

    # Ir al primer resultado
    for _ in range(YOUTUBE_MUSIC_TABS):
        keyboard.press_and_release("tab")
        time.sleep(0.12)

    keyboard.press_and_release("enter")

    return f"Reproduciendo {busqueda}."