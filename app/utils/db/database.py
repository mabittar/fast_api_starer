
from typing import Any
from sqlalchemy.ext.declarative import declarative_base


from env_config import settings
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool


engine = create_engine(
    settings.db_url, pool_size=settings.db_pool_size, poolclass=QueuePool, pool_pre_ping=True)


SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)


def get_db():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception as exc:
        session.rollback()
        raise exc
    finally:
        session.close()


Base = declarative_base()
