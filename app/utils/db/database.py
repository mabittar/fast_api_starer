
from typing import Any, Generator
from sqlalchemy.ext.declarative import declarative_base


from env_config import settings
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool


engine = create_engine(
    settings.db_url, connect_args={"check_same_thread": False}, pool_size=settings.db_pool_size, poolclass=QueuePool, pool_pre_ping=True)


SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)


Base = declarative_base()
