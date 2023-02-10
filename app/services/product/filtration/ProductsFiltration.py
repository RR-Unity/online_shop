from app.models.modelBase import ModelBase


class ProductsFiltration(ModelBase):
    name: str | None
    price: float | None
