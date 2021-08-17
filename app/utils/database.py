from contextlib import contextmanager

from env_config import settings
from sqlalchemy.engine import Engine
from sqlalchemy.engine import create_engine as _create_engine
from sqlalchemy.orm import Session, scoped_session, sessionmaker
from sqlalchemy.pool import QueuePool


class DBConnector:
    engine: Engine
    Session: scoped_session

    @classmethod
    def create_engine(cls):
        cls.engine = _create_engine(
            settings.db_url, pool_size=settings.db_pool_size, poolclass=QueuePool
        )
        cls.Session = scoped_session(sessionmaker(bind=cls.engine))

    @classmethod
    def create_session(cls) -> Session:
        session_class = scoped_session(
            sessionmaker(bind=cls.create_engine(), autoflush=True)
        )
        return session_class()

    @classmethod
    def dispose_engine(cls):
        cls.engine.dispose()

    @classmethod
    @contextmanager
    def session_scope(cls):
        """Provide a transactional scope around a series of operations."""
        session = cls.Session()
        try:
            yield session
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
