from app.models.modelBase import ModelBase


class Product(ModelBase):
    id: int = None
    name: str
    price: float
