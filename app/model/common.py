import datetime
from typing import Optional

from pydantic import BaseModel, Field, validator
from pydantic.types import PositiveInt


class DateTimeModelMixin(BaseModel):
    created_at: datetime.datetime = Field(
        None, alias="created_at")
    updated_at: datetime.datetime = Field(
        None, alias="updated_at")
    

    @validator("created_at", "updated_at", pre=True)
    def default_datetime(
        cls,
        value: datetime.datetime,
    ) -> datetime.datetime:
        return value or datetime.datetime.now()


class IDModelMixin(BaseModel):
    id_: int = Field(0, alias="id", example='1')


class Pagination(BaseModel):
    page: Optional[PositiveInt] = Field(
        1, alias="page", description="page for pagination GET", example=1)
    max_pagination: int = Field(
        10, ge=1, le=20, alias="max_pagination", example=10, description="max return for page on GET")
