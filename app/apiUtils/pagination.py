from typing import TypeVar, Callable, Any
from functools import wraps
import inspect

from fastapi import Query
from pydantic import BaseModel

from app.core.config import get_config

FuncType = TypeVar('FuncType', bound=Callable[..., Any])
config = get_config()


class Pagination(BaseModel):
    page: int = Query(1, ge=1)
    size: int | None = Query(
        config.def_items_on_page,
    )


def paginator():
    def decorator(func: FuncType):
        func.__signature__ = _get_siganture(func)   # noqa: WPS609
        paginator_keys = _get_paginator_keys()

        @wraps(func)
        def wrapper(
            *args,
            **kwargs,
        ):
            for paginator_key in paginator_keys:
                del kwargs[paginator_key]   # noqa: WPS100
            return func(*args, **kwargs)
        return wrapper
    return decorator


def _get_siganture(func: FuncType):
    sig_paginator = inspect.signature(Pagination)
    func_sig = inspect.signature(func)

    args = []
    for parameter in func_sig.parameters.values():
        args.append(parameter)

    for parameter in sig_paginator.parameters.values():  # noqa: WPS440
        args.append(parameter)
    return inspect.Signature(args)


def _get_paginator_keys():
    sig_paginator = inspect.signature(Pagination)
    return sig_paginator.parameters.keys()
