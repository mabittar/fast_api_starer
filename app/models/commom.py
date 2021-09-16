
from typing import Optional
from pydantic.types import UUID4, PositiveInt
from sqlmodel.main import Field, SQLModel
from datetime import datetime

class Pagination(SQLModel):
    page: Optional[PositiveInt] = 1
    max_pagination: int = 10


class CreatedAtModel(SQLModel):
    public_key: UUID4
    created_at: datetime = Field(
        None, alias="created_at")


class UpdateAtModel(SQLModel):
    updated_at: Optional[datetime] = Field(
        None, alias="updated_at")


class IDModel(SQLModel):
    id_: int = Field(
        default=None, 
        primary_key=True, 
        alias="id")
