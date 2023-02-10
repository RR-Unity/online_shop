from pydantic import BaseModel

from app.core.logging.enums.loggerOperationType import LoggerOperationType


class LoggerExtra(BaseModel):
    operation_type: LoggerOperationType = None
    entity_type: str = None
    task_name: str = None
    model_changes: dict = None
    msg_extra: str = None

    @classmethod
    def get_extra_fields(cls):
        return cls.__fields__
