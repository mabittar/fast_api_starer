from sqlalchemy import Column, Integer
from utils.database import Base

class PointModel(Base):
    __tablename__ = "point_model"
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



