import datetime

from pydantic import BaseModel, Field, validator


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
