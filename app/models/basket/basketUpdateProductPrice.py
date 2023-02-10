from app.models.modelBase import ModelBase


class BasketUpdateProductCount(ModelBase):
    product_id: int
    count: int
