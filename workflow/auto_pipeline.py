from autovideo.logger import get_logger
from autovideo.audio import tts, transcription
from autovideo.video import editor, davinci
from autovideo.workflow.script_parser import parse_script

logger = get_logger()

def run_pipeline(script_text: str, assets_dir: str, output_path: str, use_davinci=False):
    try:
        logger.info("Starting video generation pipeline")
        
        # Step 1: Text-to-Speech
        audio_path = tts.text_to_speech(script_text)

        # Step 2: Parse script to timeline blocks
        blocks = parse_script(script_text)

        # Step 3: Generate Video (DaVinci or MoviePy)
        if use_davinci:
            davinci.create_timeline(blocks, audio_path, assets_dir)
        else:
            editor.compose_video_ffmpeg(blocks, audio_path, assets_dir, output_path)

        logger.success("Video generation complete!")

    except Exception as e:
        logger.exception(f"Pipeline failed: {e}")
