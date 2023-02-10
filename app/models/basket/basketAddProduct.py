from app.models.modelBase import ModelBase


class BasketAddProduct(ModelBase):
    product_id: int
    count: int
