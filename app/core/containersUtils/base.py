from app.core.logging.logger import AppLogger
from app.core.config import get_config
from app.database.db import AsyncDb


def get_di_config():
    return get_config()


def get_di_logger(providers, config):
    return providers.Singleton(
        AppLogger,
        level=config.logger_level,
    )


def get_database(providers, config):
    return providers.Singleton(
        AsyncDb,
        db_url=config.db_url,
        debug=config.debug,
    )
