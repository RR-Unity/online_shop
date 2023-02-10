from app.models.modelBase import ModelBase


class Basket(ModelBase):
    id: int = None

    product_id: int
    count: int

    total_price: float
