"""
===========================================
GRASSHOPPER AI
Archivo de configuración
===========================================
"""
# ==========================================
# YOUTUBE MUSIC
# ==========================================

# Tiempo de espera para que cargue la página (segundos)
YOUTUBE_MUSIC_LOAD_TIME = 4

# Número de TAB hasta el primer resultado
YOUTUBE_MUSIC_TABS = 24


# ==========================================
# INFORMACIÓN DEL ASISTENTE
# ==========================================

ASSISTANT_NAME = "Marcos"
VERSION = "1.0"
WAKE_WORD = "grasshopper"

# ==========================================
# RECONOCIMIENTO DE VOZ
# ==========================================

LANGUAGE = "es-ES"

LISTEN_TIMEOUT = 10
PHRASE_TIME_LIMIT = 15

# ==========================================
# CONFIGURACIÓN DEL MICRÓFONO
# ==========================================

ENERGY_THRESHOLD = 300
DYNAMIC_ENERGY = True
PAUSE_THRESHOLD = 0.8

# ==========================================
# VOZ DEL ASISTENTE
# ==========================================

VOICE = "es-ES-ElviraNeural"

# ==========================================
# RUTAS DE PROGRAMAS
# ==========================================

VSCODE = r"C:\Users\gesu2\AppData\Local\Programs\Microsoft VS Code\Code.exe"

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# ==========================================
# PÁGINAS WEB
# ==========================================

CHATGPT_URL = "https://chatgpt.com"

GOOGLE_URL = "https://www.google.com"

YOUTUBE_URL = "https://www.youtube.com"

# ==========================================
# CARPETAS DEL PROYECTO
# ==========================================

PROJECTS_FOLDER = r"C:\Users\gesu2\Desktop\codigo-asier"

TEMP_FOLDER = "temp"

LOG_FOLDER = "logs"

SOUNDS_FOLDER = "sonidos"

# ==========================================
# MENSAJES DEL SISTEMA
# ==========================================

WELCOME_MESSAGE = (
    f"Hola. Soy {ASSISTANT_NAME}. "
    "Estoy listo para ayudarte."
)

GOODBYE_MESSAGE = (
    "Hasta luego."
)
