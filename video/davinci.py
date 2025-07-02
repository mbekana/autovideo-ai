import os
import sys
from autovideo.logger import get_logger

logger = get_logger()

# Resolve Scripting module path (Ubuntu default)
SCRIPTS_PATH = "/opt/resolve/Developer/Scripting/Modules/"
if SCRIPTS_PATH not in sys.path:
    sys.path.append(SCRIPTS_PATH)

try:
    import DaVinciResolveScript as bmd
except ImportError:
    raise ImportError(
        "DaVinci Resolve Scripting module not found. "
        "Make sure Resolve is installed and the SCRIPTS_PATH is correct."
    )

def create_timeline(blocks, audio_path, assets_dir):
    logger.info("Connecting to DaVinci Resolve on Ubuntu")

    resolve = bmd.scriptapp("Resolve")
    if resolve is None:
        raise RuntimeError("Could not connect to DaVinci Resolve. Is it running?")

    pm = resolve.GetProjectManager()
    project = pm.GetCurrentProject()
    if project is None:
        raise RuntimeError("No current project open in DaVinci Resolve.")

    media_pool = project.GetMediaPool()
    timeline = project.GetCurrentTimeline() or media_pool.CreateEmptyTimeline("AutoTimeline")

    logger.info("Importing clips to media pool...")

    for block in blocks:
        media_file = os.path.join(assets_dir, block["clip"])
        if not os.path.exists(media_file):
            logger.warning(f"Missing media: {media_file}")
            continue
        media_pool.ImportMedia(media_file)

    logger.success("Media imported into DaVinci timeline.")
