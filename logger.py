from loguru import logger

logger.add("logs/pipeline.log", rotation="1 MB", retention="7 days")

def get_logger():
    return logger
