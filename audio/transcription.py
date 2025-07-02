import whisper
from autovideo.logger import get_logger

logger = get_logger()
model = whisper.load_model("base")

def transcribe_audio(audio_path):
    logger.info(f"Transcribing: {audio_path}")
    result = model.transcribe(audio_path)
    return result['text']
