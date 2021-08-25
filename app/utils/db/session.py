from env_config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy.pool import QueuePool
from typing import Generator


engine = create_engine(
    settings.db_url, pool_size=settings.db_pool_size, poolclass=QueuePool, pool_pre_ping=True)


SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)


def get_db() -> Generator:
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception as exc:
        session.rollback()
        raise exc
    finally:
        session.close()
