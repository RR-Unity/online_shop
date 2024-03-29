from fastapi import FastAPI
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)
from fastapi.staticfiles import StaticFiles


def docs_router(app: FastAPI):
    app.mount('/static', StaticFiles(directory='static'), name='static')

    @app.get('/docs', include_in_schema=False)
    async def custom_swagger_ui_html():  # noqa: WPS430
        return get_swagger_ui_html(
            openapi_url=app.openapi_url,
            title='{0} - Swagger UI'.format(app.title),
            oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
            swagger_js_url='/static/swagger-ui-bundle.js',
            swagger_css_url='/static/swagger-ui.css',
        )

    @app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
    async def swagger_ui_redirect():  # noqa: WPS430
        return get_swagger_ui_oauth2_redirect_html()

    @app.get('/redoc', include_in_schema=False)
    async def redoc_html():  # noqa: WPS430
        return get_redoc_html(
            openapi_url=app.openapi_url,
            title='{0} - ReDoc'.format(app.title),
            redoc_js_url='/static/redoc.standalone.js',
        )
