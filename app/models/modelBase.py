from pydantic import BaseModel


class ModelBase(BaseModel):
    @classmethod
    def from_model(cls, model: BaseModel):
        return cls(**model.dict())

    class Config(object):
        orm_mode = True
        validate_assignment = True
