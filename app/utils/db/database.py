
from typing import Optional
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import Session


from env_config import settings
from sqlalchemy.engine import create_engine, Engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.pool import QueuePool


class SQLConnector:
    engine: Optional[Engine] = None

    @classmethod
    def get_engine(cls) -> Engine:
        engine = create_engine(
        settings.DB_URL, 
        pool_size=settings.DB_POOL_SIZE, 
        poolclass=QueuePool, 
        pool_pre_ping=True,
        connect_args={"check_same_thread": False},
        )
        return engine

    @classmethod
    def create_session(cls) -> Session:
        SessionLocal = scoped_session(
            sessionmaker(autocommit=False, autoflush=True, bind=cls.get_engine())
            )
        return SessionLocal

    @classmethod
    def close(cls) -> None:
        if cls.engine:
            cls.engine.dispose()
        cls.engine = None

Base = declarative_base()
