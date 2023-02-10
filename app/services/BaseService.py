from app.api.errors import EntityNotFound, EntityExists, IncorrectValue
from app.models.modelBase import ModelBase


class BaseService(object):
    # validations
    def _validate_is_exists(self, model: ModelBase | bool, model_name: str):
        if not model:
            raise EntityNotFound(model_name)

    def _validate_is_not_exists(self, model: ModelBase | bool, model_name: str):
        if model:
            raise EntityExists(model_name)

    def _validate_number_value(self, model_field_name: str, value: int | float, check_zero: bool = False):
        message = (
            f'The value for the field {model_field_name} must be positive.'
            f'The passed value={value} is not suitable'
        )
        if check_zero:
            if value <= 0:
                raise IncorrectValue(message=message)
        else:
            if value < 0:
                raise IncorrectValue(message=message)
