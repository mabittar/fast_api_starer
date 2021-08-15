from typing import Optional

from sqlalchemy.engine import Engine
from sqlalchemy.engine import create_engine as _create_engine
from sqlalchemy.orm import Session, scoped_session, sessionmaker
from sqlalchemy.pool import QueuePool
from env_config import settings


class DBConnector:
    engine: Optional[Engine]

    @classmethod
    def create_engine(cls) -> Engine:
        engine = _create_engine(
            settings.bd_url,
            pool_size=settings.db_pool_size,
            poolclass=QueuePool
        )
        return engine

    @classmethod
    def create_session(cls) -> Session:
        session_class = scoped_session(
            sessionmaker(bind=cls.create_engine(), autoflush=True)
        )
        return session_class()

    @classmethod
    def close(cls) -> None:
        if cls.engine:
            cls.engine.dispose()
        cls.engine = None
