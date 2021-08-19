from sqlalchemy import Column,Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class PointModel(Base):
    __tablename__ = "Point"
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
