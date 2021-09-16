from typing import Optional
from pydantic.networks import EmailStr
from datetime import datetime
from pydantic.types import UUID4
from sqlmodel import SQLModel, Field
from sqlalchemy import  Enum
from sqlmodel.main import Relationship

from models.commom import CreatedAtModel, IDModel, Pagination, UpdateAtModel
from models.point_model import Point, PointCreate


class GenderEnum(str, Enum):
    male = "male"
    female = "female"
    other = "other"
    not_given = "not_given"


class ExampleBase(SQLModel):
    name: str = Field(..., max_length=256, description="User name",
                      alias="name")
    email: EmailStr = Field(alias="email", description="User Email"
                            )
    gender: GenderEnum = Field(...,
                               description="Enumerator Class Model", alias="gender")
    float_number: float = Field(
        ..., multiple_of=0.01, description="A float Number", alias="float_number"
    )
    optional_integer: Optional[int] = Field(
        None, description="An optional positive integer",  alias="optional_integer"
    )
    optional_float: Optional[float] = Field(
        None, description="An optional float", alias="optional_float"
    )
    point: Optional[Point] = Relationship(back_populates="Point")


class ExamplePointId(ExampleBase):
    point_id: Optional[int] = Field(default=None, foreign_key="point.id")

class Example(ExampleBase, IDModel, UpdateAtModel, CreatedAtModel, table=True):
    pass

class ExampleUpdate(ExampleBase, UpdateAtModel):
    pass


class ExampleGet(ExamplePointId, Pagination, CreatedAtModel):
    pass

class ExampleCreate(ExampleBase):
    pass
