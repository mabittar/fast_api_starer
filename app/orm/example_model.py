import datetime
from typing import List, Optional
import pydantic
from pydantic.types import constr
from sqlalchemy import Column, Integer, DateTime, String, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
import pydantic
from sqlalchemy.sql.sqltypes import ARRAY
from utils.errors import OptionalNumbersError


Base = declarative_base()


class BaseClassExampleORM(Base):
    __tablename__ = 'BaseClass'
    '''Represents a basic ORM model'''
    id = Column(
        Integer, primary_key=True, unique=True, autoincrement=True, nullable=False
    )
    public_key = Column(String(36), index=True, nullable=False)
    name = Column(String(150), nullable=False)
    float_number = Column(DECIMAL(19, 2), nullable=False)
    optional_integer = Column(Integer)
    optional_float = Column(DECIMAL(19, 2))
    updated_at = Column(DateTime, default=datetime.datetime.now(
        datetime.timezone(offset=datetime.timedelta(hours=-3))))
    created_at = Column(DateTime, default=datetime.datetime.now(
        datetime.timezone(offset=datetime.timedelta(hours=-3))), nullable=False)
    domains = Column(ARRAY(String(255)))


class BaseClassExample(pydantic.BaseModel):
    '''Represents a basic model'''
    id: int 
    public_key: str(pydantic.constr(max_length=20))
    name: str(pydantic.constr(max_length=150))
    float_number: float
    optional_integer: Optional[int] = Column(Integer())
    optional_float: Optional[float] = Column(DECIMAL(19, 2))
    updated_at: datetime
    created_at = datetime
    domains = List[constr(max_length=255)]

    class Config:
        '''Pydantic configuration class'''
        allow_mutation = False
        anystr_lower = True
        orm_mode = True


    @pydantic.root_validator(pre=True)
    @classmethod
    def optional_numbers_must_be_null(cls, values):
        if (optional_integer and optional_float) not in values:
            raise OptionalNumbersError(
                title=values["title"],
                message="Model must have one optiona value"
            )
        