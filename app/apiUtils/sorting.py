from enum import Enum
from functools import wraps

from pydantic import root_validator

from app.models.modelBase import ModelBase


def extend_enum(inherited_enum):
    @wraps(inherited_enum)
    def wrapper(added_enum):
        joined = {}
        for first_item in inherited_enum:
            joined[first_item.name] = first_item.value
        for second_item in added_enum:
            joined[second_item.name] = second_item.value
        return Enum(added_enum.__name__, joined)
    return wrapper


class SortingDirection(Enum):
    asc = 'asc'
    desc = 'desc'


class SortingParams(ModelBase):
    order_by: Enum
    order_dir: SortingDirection | None = SortingDirection.asc

    @root_validator(pre=True)
    def checking_for_solid(cls, values: dict):
        order_by = values.get('order_by')

        if order_by:
            return values

        values['order_dir'] = None
        return values


def sorting_model(available_fields_enum):
    class ModifiedSortingParams(SortingParams):
        order_by: available_fields_enum | None

    return ModifiedSortingParams
