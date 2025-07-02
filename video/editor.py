import ffmpeg
from autovideo.logger import get_logger

logger = get_logger()

def compose_video_ffmpeg(blocks, audio_path, assets_dir, output_path):
    try:
        logger.info("Composing video using FFmpeg")
        # For demo: concatenate fixed clips, add audio
        input_videos = [f"{assets_dir}/{block['clip']}" for block in blocks]
        with open("inputs.txt", "w") as f:
            for clip in input_videos:
                f.write(f"file '{clip}'\n")
        
        ffmpeg.input("inputs.txt", format='concat', safe=0).output(
            output_path, vcodec='libx264', acodec='aac', shortest=None
        ).run(overwrite_output=True)

        logger.info("Video composition complete")
    except ffmpeg.Error as e:
        logger.error(e.stderr.decode())
        raise
