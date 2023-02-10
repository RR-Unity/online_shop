from app.core.logging.logger import AppLogger
from app.core.config import get_config

config = get_config()

logger = AppLogger(
    level=config.logger_level
)


def get_logger():
    return logger
