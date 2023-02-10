from fastapi import FastAPI

from app import routers


def add_routers(app: FastAPI):
    app.include_router(routers.products_router)
    app.include_router(routers.basket_router)
