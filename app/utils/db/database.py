
from typing import Optional
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import Session

from sqlmodel import SQLModel
from env_config import settings
from sqlalchemy.engine import create_engine, Engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool


class SQLConnector:
    engine: Optional[Engine] = None

    @classmethod
    def get_engine(cls) -> Engine:
        engine = create_async_engine(
        settings.DB_URL, 
        pool_size=settings.DB_POOL_SIZE, 
        poolclass=QueuePool,
        echo=True, 
        future=True
        )
        return engine

    @classmethod
    async def init_db(cls):
        async with cls.get_engine() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)

    @classmethod
    async def get_session(cls) -> AsyncSession:
        async_session = sessionmaker(
            cls.get_engine(), class_=AsyncSession, expire_on_commit=False
        )
        async with async_session() as session:
            yield session


Base = declarative_base()
