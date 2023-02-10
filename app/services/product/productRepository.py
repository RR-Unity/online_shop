from sqlalchemy import select

from app.database.baseRepository import BaseRepository
from app.database.entities.productEntity import ProductEntity

from app.models.product.productAdd import ProductAdd
from app.models.product.product import Product

from app.services.product.filtration.ProductsFiltration import ProductsFiltration
from app.services.product.filtration.products_filtration import products_filtration


class ProductRepository(BaseRepository[Product]):
    model = Product
    entity = ProductEntity

    async def create_product(self, data: ProductAdd) -> Product:
        return await self.create_by_entity_instance(model=data, entity_instance=ProductEntity)

    async def get_list_products(self, page, page_size, filtration: ProductsFiltration) -> tuple[list[Product], int]:
        async with self.db_session() as session:
            where = self._get_where_conditions(
                director=products_filtration,
                params=filtration,
            )

            query = select(ProductEntity).where(
                *where
            )

            query = self.add_pagination(query, page, page_size)
            result = await session.execute(query)
            models = self.get_list(result.scalars().unique())
            total = await self.get_total(session, query)

            return models, total
