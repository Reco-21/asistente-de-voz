
"""
===========================================
GRASSHOPPER AI
Módulo de voz
===========================================
"""

import asyncio
import edge_tts
import pygame
import os

from config import VOICE, TEMP_FOLDER

# Inicializar el reproductor de audio
pygame.mixer.init()


async def generar_audio(texto, archivo):
    """
    Genera un archivo MP3 con la voz de Microsoft Edge-TTS.
    """
    communicate = edge_tts.Communicate(
        text=texto,
        voice=VOICE
    )

    await communicate.save(archivo)


def hablar(texto):
    """
    Convierte un texto en voz y lo reproduce.
    """

    print(f"\nGrasshopper: {texto}")

    # Crear la carpeta temporal si no existe
    os.makedirs(TEMP_FOLDER, exist_ok=True)

    archivo = os.path.join(TEMP_FOLDER, "voz.mp3")

    # Generar el audio
    asyncio.run(generar_audio(texto, archivo))

    # Reproducirlo
    pygame.mixer.music.load(archivo)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.wait(100)

    pygame.mixer.music.unload()

    # Eliminar el MP3 temporal
    try:
        os.remove(archivo)
    except PermissionError:
        pass