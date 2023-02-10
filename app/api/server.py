from fastapi import FastAPI

from app.api.docs import docs_tags
from app.api.docs_router import docs_router
from app.api.exceptions import add_exceptions
from app.api.routers import add_routers
from app.core.config import get_config
from app.core.logging.get_sever_logger import get_server_logger

config = get_config()


def create_api_server() -> FastAPI:
    app = FastAPI(
        root_path=config.api_prefix,
        openapi_tags=docs_tags,
        docs_url=None,
        redoc_url=None,
        title='OELP',
        version='1.0.0',
    )
    app.logger = get_server_logger()

    add_exceptions(app)
    add_routers(app)
    docs_router(app)

    return app
