import requests
from autovideo.logger import get_logger

logger = get_logger()

def text_to_speech(text, output_path="output.mp3"):
    logger.info("Generating TTS audio using TTSMaker")
    url = "https://api.ttsmaker.com/v1/generate"
    payload = {
        "text": text,
        "voice": "en_us_001",  # TTSMaker voice ID
        "output_format": "mp3"
    }
    r = requests.post(url, json=payload)
    
    if r.status_code == 200 and 'audio_url' in r.json():
        audio_url = r.json()['audio_url']
        audio = requests.get(audio_url)
        with open(output_path, 'wb') as f:
            f.write(audio.content)
        logger.success("TTS audio saved")
        return output_path
    else:
        logger.error("TTSMaker failed: " + str(r.text))
        return None
