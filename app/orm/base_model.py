import datetime
from sqlalchemy import Column, Integer, DateTime, String, func
from sqlalchemy.ext.declarative import declarative_base


class BaseModel:
    id = Column(
        Integer, primary_key=True, unique=True, autoincrement=True, nullable=False
    )
    updated_at = Column(DateTime, default=datetime.datetime.now(datetime.timezone(offset=datetime.timedelta(hours=-3))), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now(
        datetime.timezone(offset=datetime.timedelta(hours=-3))), nullable=False)

    def __init__(self) -> None:
        super().__init__()


BaseModel = declarative_base(cls=BaseModel)
