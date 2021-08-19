import uuid
from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import Optional, Union

import pydantic
from pydantic import BaseModel, Field
from pydantic.networks import EmailStr
from pydantic.types import PositiveInt, condecimal, conint
from typing_extensions import Annotated
from utils.errors import OptionalNumbersError


class GenderEnum(str, Enum):
    male = "male"
    female = "female"
    other = "other"
    not_given = "not_given"


class Point(BaseModel):
    x: int
    y: int

    class Config:
        title = "Point Model"
        orm_mode = True


class ExampleClassRequest(BaseModel):
    """Represents a Resquest for basic Example Endpoint"""

    public_key: Optional[Union[int, str, uuid.UUID]]
    name: Annotated[str, Field(alias="User Name", max_length=256,
                               description="User name", example="John Lennon")]

    gender: Annotated[GenderEnum, Field(description="Enumerator Class Model", alias="Gender")]
    email: Annotated[EmailStr, Field(alias="user email", description="User Email", example="john@beatles.com"
    )]
    float_number: Decimal = Field(
        ..., multiple_of=0.01, description="A float Number", example="1.11"
    )
    optional_integer: Optional[PositiveInt] = Field(
        None, description="An optional positive integer", example="11"
    )
    optional_float: Optional[condecimal(max_digits=18, decimal_places=2)] = Field(
        None, description="An optional float", example="0.12"
    )
    point: Optional[Point] = Field(..., alias="point",
                                   description="example of relationship model. Set X and Y")
    page: Optional[PositiveInt] = Field(
        1, alias="page", description="page for pagination GET")
    max_pagination: int = Field(
        10, ge=1, le=20, alias="max_pagination", description="max return for page on GET")

    class Config:
        title = "Exemple Model"
        orm_mode = True

    # @pydantic.root_validator(pre=True)
    # @classmethod
    # def optional_numbers_must_be_null(cls, values):
    #     if ("optional_integer" and "optional_float") not in values:
    #         raise OptionalNumbersError(
    #             title=values["title"], message="Model must have one optional value"
    #         )

    # @pydantic.validator('email')
    # @classmethod
    # def email_must_contains_at(cls, values):
    #     if "@" not in values:
    #         raise OptionalNumbersError(
    #             title=values["title"], message="Model must have one optional value"
    #         )


class ExampleClassResponse(BaseModel):
    """Represents a Response for example endpoint"""

    id: int
    public_key: Annotated[
        Union[int, str, uuid.UUID],
        Field(alias="public key",
              description="String identification",
              example=uuid.uuid4()
              )
    ]
    name: str
    gender: GenderEnum
    email: str
    float_number: condecimal(max_digits=18, decimal_places=2)
    optional_integer: Optional[PositiveInt]
    optional_float: Optional[Decimal]
    output_optional: Optional[condecimal(
        max_digits=18, decimal_places=2)]
    point: Optional[Point]
    updated_at: Optional[datetime]
    updated_at: Optional[datetime] = Field(
        None, alias="update at", description="updated at")
    created_at: datetime = Field(
        default_factory=datetime.now, alias="create at")
    page: Optional[PositiveInt]
    max_pagination: Optional[PositiveInt]
