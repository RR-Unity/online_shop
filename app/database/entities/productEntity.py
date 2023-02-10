import sqlalchemy as sa

from app.database.base import Base
from app.database.entityBase import EntityBase
from app.models.product.product import Product


class ProductEntity(Base, EntityBase[Product]):
    __tablename__ = 'products'

    not_required_fields = {'meta'}
    model = Product

    id = sa.Column(sa.Integer(), sa.Identity(), primary_key=True, nullable=False)
    name = sa.Column(sa.VARCHAR(), nullable=False)
    price = sa.Column(sa.Float(), nullable=False)
