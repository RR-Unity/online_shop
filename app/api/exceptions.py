from fastapi import Request, status, FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from app.api.errors import AppBaseException
from app.core.logger import get_logger

logger = get_logger()


def add_exceptions(app: FastAPI):
    @app.exception_handler(ValidationError)
    async def validation_exception_handler(  # noqa: WPS430
        request: Request,
        exc: ValidationError,
    ):
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content=jsonable_encoder({'detail': exc.errors()}),
        )

    @app.exception_handler(AppBaseException)
    async def http_exception_handler(  # noqa: WPS430
            request: Request,
            exc: AppBaseException,
    ):
        return JSONResponse(
            status_code=exc.status_code,
            content=jsonable_encoder({
                'detail': exc.detail,
                **exc.get_extra_fields(),
            }),
        )

    @app.exception_handler(Exception)
    async def exception_logger_handler(  # noqa: WPS430, F811
        request: Request,
        exc: Exception,
    ):
        logger.exception(exc)
        raise exc
