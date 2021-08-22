
from sqlalchemy import DECIMAL, Column, DateTime, Enum, Integer, String, func, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
class PointModel(Base):
    __tablename__ = "PointModel"
    """Represents a relantionship ORM model"""
    id = Column(
        Integer,
        primary_key=True,
        unique=True,
        index=True,
        autoincrement=True,
        nullable=False,
    )
    x = Column(Integer, nullable=False)
    y = Column(Integer, nullable=False)


class ExampleClassModel(Base):
    __tablename__ = "ExampleClassModel"
    """Represents a basic ORM model"""
    id = Column(
        Integer,
        primary_key=True,
        unique=True,
        index=True,
        autoincrement=True,
        nullable=False,
    )
    public_key = Column(String(36), index=True, nullable=False)
    name = Column(String(150), nullable=False)
    email = Column(String(150))
    gender = Column(Enum("male", "female", "other",
                    "not_given"), nullable=False)
    float_number = Column(DECIMAL(19, 2), nullable=False)
    optional_integer = Column(Integer, nullable=True)
    optional_float = Column(DECIMAL(19, 2), nullable=True)
    point_id = Column(Integer, ForeignKey(PointModel.id))
    point = relationship("PointModel", foreign_keys=[
                         point_id], lazy="joined")
    updated_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
