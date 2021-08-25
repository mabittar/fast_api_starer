
from sqlalchemy import DECIMAL, Column, DateTime, Enum, Integer, String, func, ForeignKey
from sqlalchemy.orm import relationship
from .point_model import Point
from utils.db.database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .point_model import Point

class Example(Base):
    __tablename__ = "Example"
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
    point_id = Column(Integer, ForeignKey(Point.id))
    point = relationship("Point", foreign_keys=[
                         point_id], lazy="joined")
    updated_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
