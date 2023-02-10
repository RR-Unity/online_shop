from dependency_injector.wiring import inject, Provide

from fastapi import APIRouter
from fastapi.params import Depends

from app.api.errors import EntityExists, EntityNotFound, ApiPermissionError
from app.api.responses import ResponseApi, ResponsePaginationApi, response

from app.apiUtils.docUtils import doc_response_errors
from app.apiUtils.pagination import Pagination

from app.core.containers import inject_module, Container
from app.models.product.productAdd import ProductAdd
from app.models.product.product import Product
from app.services.product.filtration.ProductsFiltration import ProductsFiltration
from app.services.product.productService import ProductService

inject_module(__name__)


products_router = APIRouter(
    tags=['products'],
    prefix='/products',
)


# LIST
@products_router.get(
    '',
    response_model=ResponsePaginationApi[list[Product]],
    responses=doc_response_errors(
        EntityNotFound('Product'),
        ApiPermissionError(),
    ),
    operation_id='GetProducts',
)
@inject
async def get_products(
        pagination: Pagination = Depends(),
        filtration: ProductsFiltration = Depends(),

        service: ProductService = Depends(Provide[Container.product_service]),
):
    result, total = await service.get_list_products(
        pagination=pagination,
        filtration=filtration,
    )

    return response(result, total, pagination)


@products_router.post(
    '',
    response_model=None,
    responses=doc_response_errors(
        EntityExists('Product'),
        ApiPermissionError(),
    ),
    operation_id='CreateProduct',
)
@inject
async def create_product(
        data: ProductAdd,
        service: ProductService = Depends(Provide[Container.product_service]),
):
    product = await service.create_product(data=data)

    return response(product)
