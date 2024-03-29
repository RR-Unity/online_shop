from typing import TypeVar, Generic, Type
from sqlalchemy.ext.declarative import declarative_base
from app.models.modelBase import ModelBase
from sqlalchemy import inspect

OrmModel = declarative_base()

Entity = TypeVar('Entity', bound=OrmModel)
Model = TypeVar('Model', bound=ModelBase)


class EntityBase(Generic[Model]):
    model: Type[Model] = None
    update_ignore_fields = {'id', 'updated_at', 'created_at', 'deleted_at', 'meta'}

    def __init__(self, *args, **kwargs):
        pass  # noqa: WPS100

    @classmethod
    def from_model(cls: Type[Entity], model: Model) -> Entity:
        data_values = {}
        colls = inspect(cls).mapper.column_attrs
        for coll in colls:
            col_name = coll.key
            try:
                data_values[col_name] = getattr(model, col_name)
            except AttributeError:
                pass  # noqa: WPS100

        return cls(**data_values)

    @classmethod
    def values_from_model(cls: Type[Entity], model: Model) -> dict:
        data_values = {}
        colls = inspect(cls).mapper.column_attrs
        for coll in colls:
            if coll.key in cls.update_ignore_fields:
                continue
            data_values[coll.key] = getattr(model, coll.key)
        return data_values

    def to_values(self) -> dict:
        data_values = {}
        colls = inspect(self).mapper.column_attrs
        for coll in colls:
            col_name = coll.key
            if col_name in self.update_ignore_fields:
                continue
            data_values[col_name] = getattr(self, col_name)
        return data_values

    def to_model(self) -> Model:
        return self.model.from_orm(self)

    @classmethod
    @property
    def soft_delete(cls) -> bool:
        return hasattr(cls, 'deleted_at')  # noqa: WPS110
