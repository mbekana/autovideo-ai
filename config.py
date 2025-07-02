import os
from dotenv import load_dotenv

load_dotenv()

TEMP_DIR = os.getenv("TEMP_DIR", "./temp")
VOICE_MODEL = os.getenv("VOICE_MODEL", "elevenlabs")
