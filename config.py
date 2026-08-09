import os


# =========================
# APP INFORMATION
# =========================

APP_NAME = "AI Virtual Assistant"
APP_VERSION = "1.0.0"


# =========================
# DATABASE
# =========================

DATABASE_NAME = "assistant.db"


# =========================
# SETTINGS
# =========================

SETTINGS_FILE = "settings.json"


# =========================
# AI API KEY
# =========================
# Keep your real API key in an environment variable.
# Never upload the real key to GitHub.

AI_API_KEY = os.getenv("AI_API_KEY", "")


# =========================
# WEATHER
# =========================

WEATHER_API_KEY = os.getenv(
    "WEATHER_API_KEY",
    ""
)


# =========================
# VOICE SETTINGS
# =========================

VOICE_ENABLED = True
VOICE_RATE = 170
VOICE_VOLUME = 1.0
