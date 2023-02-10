import math

from typing import Generic, TypeVar, Any
from pydantic.generics import GenericModel

from app.apiUtils.pagination import Pagination

DataT = TypeVar('DataT')


class ResponseApi(GenericModel, Generic[DataT]):
    payload: DataT


class ResponsePaginationApi(ResponseApi, Generic[DataT]):
    pages: int = 0
    page: int = 0
    total: int = 0


def response(payload: Any, total: int = None, pagination: Pagination = None):
    if total is not None and pagination is not None:
        return ResponsePaginationApi(
            payload=payload,
            pages=math.ceil(total / pagination.size),
            page=pagination.page,
            total=total,
        )

    return ResponseApi(payload=payload)
