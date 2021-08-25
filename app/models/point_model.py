from typing import TYPE_CHECKING
from sqlalchemy import Column, Integer
from utils.db.database import Base


if TYPE_CHECKING:
    from .example_model import Example

class Point(Base):
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



