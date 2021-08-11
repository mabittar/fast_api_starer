from typing import Optional
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine, create_engine as _create_engine
from sqlalchemy.orm import sessionmaker, Session, scoped_session
from sqlalchemy.pool import QueuePool
from api.utils.constants import DATABASE_URL, DB_POOL_SIZE

class SQLConnector:
    engine: Optional[Engine]

    @classmethod
    def create_engine(cls) -> Engine:
        engine = _create_engine(
            DATABASE_URL,
            pool_size=DB_POOL_SIZE,
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

