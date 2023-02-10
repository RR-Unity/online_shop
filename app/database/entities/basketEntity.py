import sqlalchemy as sa
from sqlalchemy import UniqueConstraint

from app.database.base import Base
from app.database.entities.productEntity import ProductEntity
from app.database.entityBase import EntityBase
from app.models.basket.basket import Basket


class BasketEntity(Base, EntityBase[Basket]):
    __tablename__ = 'basket'
    __table_args__ = (
        UniqueConstraint('product_id'),
    )
    not_required_fields = {'meta'}
    model = Basket

    id = sa.Column(sa.Integer(), sa.Identity(), primary_key=True, nullable=False)

    product_id = sa.Column(
        sa.Integer(),
        sa.ForeignKey(ProductEntity.id, ondelete='RESTRICT', onupdate='RESTRICT'),
        nullable=False,
    )
    count = sa.Column(sa.Integer(), nullable=False)
    total_price = sa.Column(sa.Float(), nullable=False)

