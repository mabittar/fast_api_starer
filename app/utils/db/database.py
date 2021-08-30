
from typing import Any, Generator
from sqlalchemy.ext.declarative import declarative_base


from env_config import settings
# from sqlalchemy.engine import create_engine
from sqlmodel import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool

from sqlmodel import SQLModel

from models import models


# engine = create_engine(
#     settings.db_url, pool_size=settings.db_pool_size, poolclass=QueuePool, pool_pre_ping=True)

engine = create_engine(settings.db_url, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)


Base = declarative_base()

# Create all models in local db
def create_db_and_tables():
    SQLModel.metadata.create_all(bind=engine, tables=models)
