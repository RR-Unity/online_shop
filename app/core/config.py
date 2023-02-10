from app.utils.envUtils import load_config
from pydantic import BaseModel

ENV_FILE = '.env'
DATABASE_FILE = 'database_version'


class Config(BaseModel):
    db_url: str
    db_url_test: str

    def_items_on_page: int

    uvicorn_workers: int
    uvicorn_host: str
    uvicorn_port: int
    api_prefix: str

    logger_level: str

    developer_mode: bool
    debug: bool

    @classmethod
    def load_config(cls) -> 'Config':
        data_env = load_config(ENV_FILE)

        return Config(
            db_url=data_env['DB_URL'],
            db_url_test=data_env['DB_URL_TEST'],

            def_items_on_page=data_env['DEF_ITEMS_ON_PAGE'],

            uvicorn_workers=data_env.get('UVICORN_WORKERS', 1),
            uvicorn_host=data_env.get('UVICORN_HOST', 'localhost'),
            uvicorn_port=data_env.get('UVICORN_PORT', 3000),
            api_prefix=data_env.get('API_PREFIX', ''),

            logger_level=data_env.get('LOGGER_LEVEL', 'INFO'),

            developer_mode=data_env.get('DEVELOPER_MODE') == 'true',
            debug=data_env.get('DEBUG') == 'true',
        )


config = Config.load_config()


def get_config():
    return config
