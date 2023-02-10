from typing import TypeVar, Generic, Callable

from pydantic import BaseModel
from sqlalchemy import update, select, delete, func

from app.database.entityBase import OrmModel
from app.models.modelBase import ModelBase

Entity = TypeVar('Entity', bound=OrmModel)
Model = TypeVar('Model', bound=ModelBase)


class BaseRepository(Generic[Model]):
    model: Model
    entity: Entity

    def __init__(self, db_session):
        self.db_session = db_session

    async def create_by_entity_instance(self, model: ModelBase, entity_instance):
        async with self.db_session() as session:
            entity = entity_instance.from_model(model)
            session.add(entity)
            await session.commit()

            await session.refresh(entity)
            return entity.to_model()

    async def save_entity(self, model, entity_instance):
        async with self.db_session() as session:
            await session.execute(
                update(entity_instance).
                where(entity_instance.id == model.id).
                values(entity_instance.values_from_model(model))  # noqa: C812
            )
            await session.commit()

    async def save(self, model: Model):
        await self.save_entity(model, self.entity)

    async def update(self, model: Model) -> Model:
        await self.save(model)
        return await self.get_by_id(model.id)

    async def delete_entity_by_id(self, model_id: int, entity_instance):
        async with self.db_session() as session:
            await session.execute(
                delete(entity_instance).where(entity_instance.id == model_id),
            )
            await session.commit()

    async def get_by_id(self, model_id: int) -> Model | None:
        return await self.get_entity_by_id(model_id, self.entity)

    async def get_entity_by_id(
        self,
        model_id: int,
        entity,
    ) -> Model | None:
        async with self.db_session() as session:
            query = select(entity).limit(1).where(
                entity.id == model_id,
            )

            result = await session.scalar(query)
            return self.model_or_none(result)

    async def get_total(self, session, query) -> int:
        query = query.offset(None).order_by(None).limit(None)
        count_stmt = select(func.count()).select_from(query.subquery())
        return await session.scalar(count_stmt)

    def get_list(self, query, model=None) -> list:
        model_to = model if model else self.model
        return [model_to.from_orm(entity) for entity in query]

    def add_pagination(self, query, page: int, page_size: int):
        return query.offset((page - 1) * page_size).limit(page_size)

    def model_or_none(self, entity):
        return entity.to_model() if entity else None

    def _get_where_conditions(
        self,
        director: Callable,
        params: BaseModel,
    ) -> list:
        builder = director(params)
        return builder.get_conditions()
