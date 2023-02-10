from typing import Set

from dependency_injector import containers, providers

from app.core.containersUtils.base import get_di_config, get_di_logger, get_database
from app.core.containersUtils.product_service import get_product_service
from app.core.containersUtils.basket_service import get_basket_service

modules: Set = set()


class Container(containers.DeclarativeContainer):
    # Base
    config = get_di_config()
    logger = get_di_logger(providers, config)
    database = get_database(providers, config)

    product_service = get_product_service(providers, database.provided.session)
    basket_service = get_basket_service(providers, database.provided.session)


container = Container()


def inject_module(module_name: str):
    modules.add(module_name)


def wire_modules():
    container.wire(modules=list(modules))
