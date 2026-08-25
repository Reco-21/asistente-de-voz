
import speech_recognition as sr

from config import (
    LANGUAGE,
    LISTEN_TIMEOUT,
    PHRASE_TIME_LIMIT,
    ENERGY_THRESHOLD,
    DYNAMIC_ENERGY,
    PAUSE_THRESHOLD
)


class Escuchador:

    def __init__(self):

        self.recognizer = sr.Recognizer()

        self.recognizer.energy_threshold = ENERGY_THRESHOLD
        self.recognizer.dynamic_energy_threshold = DYNAMIC_ENERGY
        self.recognizer.pause_threshold = PAUSE_THRESHOLD

        self.microfono = sr.Microphone()

        print("🎤 Calibrando micrófono...")

        with self.microfono as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=1)

        print("✅ Micrófono listo.\n")


    def escuchar(self):

        with self.microfono as source:

            print("🎤 Escuchando...")

            try:

                audio = self.recognizer.listen(
                    source,
                    timeout=LISTEN_TIMEOUT,
                    phrase_time_limit=PHRASE_TIME_LIMIT
                )

            except sr.WaitTimeoutError:
                return ""

        try:

            texto = self.recognizer.recognize_google(
                audio,
                language=LANGUAGE
            )

            texto = texto.lower().strip()

            print(f"👤 Tú: {texto}")

            return texto

        except sr.UnknownValueError:
            print("❌ No he entendido.")
            return ""

        except sr.RequestError:
            print("❌ Error al conectar con Google.")
            return ""

        except Exception as e:
            print("❌ Error:", e)
            return ""