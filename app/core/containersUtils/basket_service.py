from app.services.basket.basketService import BasketService
from app.services.basket.basketRepository import BasketRepository


def get_basket_service(providers, session):
    repository = providers.Factory(
        BasketRepository,
        db_session=session,
    )

    return providers.Factory(
        BasketService,
        repository=repository,
    )
