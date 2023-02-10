from sqlalchemy import select

from app.database.baseRepository import BaseRepository

from app.database.entities.basketEntity import BasketEntity
from app.database.entities.productEntity import ProductEntity

from app.models.basket.basket import Basket
from app.models.product.product import Product


class BasketRepository(BaseRepository[BasketEntity]):
    model = Basket
    entity = BasketEntity

    async def get_product_by(self, product_id: int) -> Product | None:
        return await self.get_entity_by_id(model_id=product_id, entity=ProductEntity)

    async def add_product_to_basket(self, basket_model: Basket) -> Basket:
        return await self.create_by_entity_instance(model=basket_model, entity_instance=BasketEntity)

    async def get_product_from_basket(self, product_id: int) -> Basket | None:
        async with self.db_session() as session:
            query = select(BasketEntity).limit(1).where(
                BasketEntity.product_id == product_id,
            )

            result = await session.scalar(query)

            return self.model_or_none(result)

    async def update_product_in_basket(self, basket_model: Basket) -> Basket:
        await self.save_entity(model=basket_model, entity_instance=BasketEntity)

        return await self.get_by_id(basket_model.id)

