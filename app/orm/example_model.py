import datetime
from decimal import Decimal
import uuid
from pydantic import BaseModel, Field
from pydantic.networks import EmailStr
from pydantic.types import UUID4
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
    email = Column(String(200), nullable=True)
    float_number = Column(DECIMAL(19, 2), nullable=False)
    optional_integer = Column(Integer)
    optional_float = Column(DECIMAL(19, 2))
    updated_at = Column(DateTime, default=datetime.datetime.now(
        datetime.timezone(offset=datetime.timedelta(hours=-3))))
    created_at = Column(DateTime, default=datetime.datetime.now(
        datetime.timezone(offset=datetime.timedelta(hours=-3))), nullable=False)
    domains = Column(ARRAY(String(255)))


class ExampleClassModel(BaseModel):
    '''Represents a basic model'''
    id: int 
    public_key: UUID4 = Field(default_factory=uuid.uuid4, title='Chave Pública')
    name: str = Field(str, title="None do representado")
    email:str =  Field(EmailStr, max_length=200, title="Email do representado")
    float_number: float = Field(Decimal(), multiple_of=0.01)
    optional_integer:int = Field(Decimal(), ge=0)
    optional_float:float = Field(Decimal())
    updated_at: datetime.datetime
    created_at: datetime.datetime = Field(
        default_factory=datetime.datetime.now)
    domains: list = Field(list)

    class Config:
        '''Pydantic configuration class'''
        allow_mutation = False
        anystr_lower = True
        orm_mode = True


    @pydantic.root_validator(pre=True)
    @classmethod
    def optional_numbers_must_be_null(cls, values):
        if ("optional_integer" and "optional_float") not in values:
            raise OptionalNumbersError(
                title=values["title"],
                message="Model must have one optional value"
            )
        
