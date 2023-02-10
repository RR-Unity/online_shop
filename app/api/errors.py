from typing import Any

from fastapi import HTTPException


class AppBaseException(HTTPException):
    extra = None

    def __init__(self, detail, status_code):
        self.extra = None

    def get_extra_fields(self) -> dict:
        if self.extra:
            return {'info': {**self.extra}}
        return {}


class ComingSoon(AppBaseException):
    def __init__(self):
        self.status_code = 500
        self.detail = 'API in developing. Will coming soon'


class ApiAccessError(AppBaseException):
    def __init__(self):
        self.status_code = 401
        self.detail = 'access denied'


class ApiPermissionError(AppBaseException):
    def __init__(self):
        self.status_code = 403
        self.detail = 'permission denied'


class EntityNotFound(AppBaseException):
    def __init__(self, entity: str = None):
        extra_message = f'{entity}' if entity else ''

        self.status_code = 452
        self.detail = f'entity {extra_message} not found(information in "entity" attribute)'
        self.entity = entity


class EntityExists(AppBaseException):
    def __init__(self, entity: str, field: str = None):
        self.status_code = 409
        self.detail = f'another entity {entity} already exists (information in "field" and "entity" attributes)'
        self.entity = entity
        self.field = field


class FilterValueError(AppBaseException):
    def __init__(self, message: str = None):
        self.status_code = 453
        self.detail = message if message else ''
        self.message = message


class CurrencyBaseNull(ValueError):
    def __init__(self, message: str = 'currency_base is Null'):
        self.status_code = 454
        self.detail = message


class CurrencyQuoteNull(ValueError):

    def __init__(self, message: str = 'currency_quote is Null'):
        self.status_code = 455
        self.detail = message


class EntityIsBound(AppBaseException):
    def __init__(self, entity: str, bound_entity: str, bound_model: Any = None):
        self.status_code = 456
        self.detail = f'entity {entity} is bound with {bound_entity}(information in entity, bound_entity, bound_model)'
        self.extra = {'entity': entity, 'bound_entity': bound_entity, 'bound_model': bound_model}


class InvalidLpCredentials(AppBaseException):
    def __init__(self, message: str, credentials: dict = None):
        self.status_code = 457
        self.detail = f'Invalid credentials: {message}'


class CommonFixError(AppBaseException):
    def __init__(self, message: str):
        self.status_code = 458
        self.detail = message


class IncorrectValue(AppBaseException):
    def __init__(self, message: str):
        self.status_code = 459
        self.detail = message
