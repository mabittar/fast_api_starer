
from sqlalchemy import DECIMAL, Column, DateTime, Enum, Integer, String, func
from sqlalchemy.sql.sqltypes import REAL

from utils.db.database import Base


class Example(Base):
    __tablename__ = "example"
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
    float_number = Column(REAL(19, 2), nullable=False)
    optional_integer = Column(Integer, nullable=True)
    optional_float = Column(REAL(19, 2), nullable=True)
    updated_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)

    # If you are using another DB engine should change REAL for DECIMALS
