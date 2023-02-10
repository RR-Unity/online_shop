from app.models.basket.basket import Basket
from app.models.basket.basketAddProduct import BasketAddProduct
from app.models.basket.basketUpdateProductPrice import BasketUpdateProductCount

from app.api.errors import EntityExists

from app.services.BaseService import BaseService
from app.services.basket.basketRepository import BasketRepository


class BasketService(BaseService):
    def __init__(self, repository: BasketRepository):
        self._repository = repository

    async def add_product_to_basket(self, data: BasketAddProduct) -> Basket:
        product = await self._repository.get_product_by(product_id=data.product_id)

        self._validate_is_exists(product, 'Products')

        product_in_basket = await self._repository.get_product_from_basket(product_id=data.product_id)

        self._validate_is_not_exists(product_in_basket, 'Products')

        self._validate_number_value(model_field_name="count", value=data.count, check_zero=True)

        basket_model = Basket(product_id=product.id, count=data.count, total_price=data.count*product.price)

        updated_basket_row = await self._repository.add_product_to_basket(basket_model)

        return updated_basket_row

    async def update_product_count_in_basket(self, data: BasketUpdateProductCount) -> Basket | str:
        product = await self._repository.get_product_by(product_id=data.product_id)

        self._validate_is_exists(product, 'Products')

        self._validate_number_value(model_field_name="count", value=data.count, check_zero=True)

        product_in_basket = await self._repository.get_product_from_basket(product_id=data.product_id)

        if not product_in_basket:
            return await self.add_product_to_basket(data=BasketAddProduct(product_id=data.product_id, count=data.count))

        if data.count == 0:
            await self._repository.delete_entity_by_id(model_id=product_in_basket.id, entity_instance=Basket)
            return "{}"

        if product_in_basket.count == data.count:
            raise EntityExists(entity='Basket')

        product_in_basket.count = data.count
        product_in_basket.total_price = data.count * product.price

        basket = await self._repository.update_product_in_basket(product_in_basket)

        return basket

