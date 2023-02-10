from dependency_injector.wiring import inject, Provide

from fastapi import APIRouter
from fastapi.params import Depends

from app.api.errors import EntityExists, EntityNotFound, ApiPermissionError
from app.api.responses import ResponseApi, ResponsePaginationApi, response

from app.apiUtils.docUtils import doc_response_errors

from app.core.containers import inject_module, Container
from app.models.basket.basket import Basket
from app.models.basket.basketAddProduct import BasketAddProduct
from app.models.basket.basketUpdateProductPrice import BasketUpdateProductCount
from app.services.basket.basketService import BasketService

inject_module(__name__)


basket_router = APIRouter(
    tags=['basket'],
    prefix='/basket',
)


@basket_router.post(
    '',
    response_model=ResponseApi[Basket],
    responses=doc_response_errors(
        EntityExists('Basket'),
        ApiPermissionError(),
    ),
    operation_id='AddProductToBasket',
)
@inject
async def add_product_to_basket(
        data: BasketAddProduct,
        service: BasketService = Depends(Provide[Container.basket_service]),
):
    product_to_basket = await service.add_product_to_basket(data=data)

    return response(product_to_basket)


@basket_router.patch(
    '',
    response_model=ResponseApi[Basket],
    responses=doc_response_errors(
        EntityExists('Basket'),
        ApiPermissionError(),
    ),
    operation_id='UpdateProductCountInBasket',
)
@inject
async def update_product_count_in_basket(
        data: BasketUpdateProductCount,
        service: BasketService = Depends(Provide[Container.basket_service]),
):
    product = await service.update_product_count_in_basket(data=data)

    return response(product)
