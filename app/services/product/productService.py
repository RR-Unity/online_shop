from app.api.errors import EntityNotFound, EntityExists
from app.apiUtils.pagination import Pagination
from app.apiUtils.sorting import sorting_model
from app.models.product.productAdd import ProductAdd
from app.services.BaseService import BaseService
from app.services.product.productRepository import ProductRepository


class ProductService(BaseService):
    def __init__(self, repository: ProductRepository):
        self._repository = repository

    async def create_product(self, data: ProductAdd):
        self._validate_number_value(model_field_name="price", value=data.price, check_zero=False)
        return await self._repository.create_product(data=data)

    async def get_list_products(self, pagination, filtration):
        products = await self._repository.get_list_products(
            page=pagination.page,
            page_size=pagination.size,
            filtration=filtration
        )

        return products
