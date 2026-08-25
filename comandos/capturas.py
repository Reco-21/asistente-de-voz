
import os
from datetime import datetime
import mss


CARPETA_CAPTURAS = "capturas"


def captura_pantalla():

    os.makedirs(CARPETA_CAPTURAS, exist_ok=True)

    nombre = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".png"

    ruta = os.path.join(CARPETA_CAPTURAS, nombre)

    with mss.mss() as sct:
        sct.shot(output=ruta)

    return ruta