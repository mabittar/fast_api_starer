from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import datetime

class Point(SQLModel, table=True):
    """Represents a basic ORM model"""
    id: Optional[int] = Field(default=None, primary_key=True)
    x: float = Field(
        ..., multiple_of=0.01, description="A float Number", alias="float_number"
    )
    y: float = Field(
        ..., multiple_of=0.01, description="A float Number", alias="float_number"
    )
    updated_at: datetime = Field(None, alias="updated_at")
    created_at: datetime = Field(alias="created_at", default_factory=datetime.utcnow)
    
