import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime, String, DECIMAL, Enum, func

Base = declarative_base()


class ExampleClassModel(Base):
    __tablename__ = 'BaseClass'
    '''Represents a basic ORM model'''
    id = Column(
        Integer, primary_key=True, unique=True, index=True, autoincrement=True, nullable=False
    )
    public_key = Column(String(36), index=True, nullable=False)
    name = Column(String(150), nullable=False)
    gender = Column(Enum("male", "female", "other",
                    "not_given"), nullable=False)
    float_number = Column(DECIMAL(19, 2), nullable=False)
    optional_integer = Column(Integer, nullable=True)
    optional_float = Column(DECIMAL(19, 2), nullable=True)
    updated_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
