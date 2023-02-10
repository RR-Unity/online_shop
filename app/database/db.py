import json

import pydantic.json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.pool import NullPool


def _custom_json_serializer(*args, **kwargs) -> str:
    """
    Encodes json in the same way that pydantic does.
    """
    return json.dumps(*args, default=pydantic.json.pydantic_encoder, **kwargs)


class AsyncDb(object):
    def __init__(self, db_url: str, debug: bool):
        engine = create_async_engine(
            db_url,
            echo=debug,
            poolclass=NullPool,
            json_serializer=_custom_json_serializer,
        )

        self.session = sessionmaker(
            engine,
            expire_on_commit=False,
            class_=AsyncSession,
        )


class Db(object):
    def __init__(self, db_url: str, debug: bool):
        engine = create_engine(
            db_url,
            echo=debug,
        )

        self.session = sessionmaker(
            engine,
            expire_on_commit=False,
        )
