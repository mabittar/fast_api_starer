
from sqlmodel import SQLModel, Field

from models.commom import CreatedAtModel, IDModel, UpdateAtModel


class PointBase(SQLModel):
    x: float = Field(
        None, description="X coordinates", alias="optional_integer"
    )
    y: float = Field(
        None, description="Y coordinates", alias="optional_integer"
    )
    


class Point(PointBase, CreatedAtModel, UpdateAtModel, IDModel, table=True):
    pass


class PointCreate(PointBase):
    pass
