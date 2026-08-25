
from config import ASSISTANT_NAME
from audio.hablar import hablar
from audio.escuchar import Escuchador
from comandos.basicos import procesar_comando


def main():

    print("=" * 50)
    print(f"        {ASSISTANT_NAME} Asistente de voz")
    print("=" * 50)

    escucha = Escuchador()

    hablar(f"Hola. Soy {ASSISTANT_NAME}.")

    while True:

        comando = escucha.escuchar()

        if comando == "":
            continue

        salir = procesar_comando(
            comando,
            hablar,
            escucha
        )

        if salir:
            break


if __name__ == "__main__":
    main()