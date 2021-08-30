
from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4
from pydantic.networks import EmailStr
from pydantic.types import condecimal
from sqlalchemy import Column, Enum
from sqlalchemy.sql.sqltypes import REAL
from sqlmodel import Field, SQLModel


class Example(SQLModel, table=True):
    """Represents a basic ORM model"""
    id: Optional[int] = Field(default=None, primary_key=True)
    public_key: UUID = Field(alias="public key", description="String identification",
                                     default_factory=uuid4()
                                                   )
    name: str = Field(..., max_length=256, description="User name", alias="name")
    email: EmailStr = Field(alias="email", description="User Email")
    gender = Column(Enum("male", "female", "other",
                    "not_given"), nullable=False)
    float_number: float = Field(
        ..., multiple_of=0.01, description="A float Number", alias="float_number"
    )
    optional_integer: int = Field(
        None, description="An optional positive integer", alias="optional_integer"
    )
    optional_float: Optional[condecimal(max_digits=18, decimal_places=2)] = Field(
        None, description="An optional float", alias="optional_float"
    )
    point_id: Optional[int] = Field(default=None, foreign_key="point.id")
    updated_at: datetime = Field(None, alias="updated_at")
    created_at: datetime = Field(alias="created_at", default_factory=datetime.utcnow)

    # If you are using another DB engine than SQLite could change REAL for DECIMALS
