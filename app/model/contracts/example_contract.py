import uuid
from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Union

import pydantic
from model.common import DateTimeModelMixin, IDModelMixin, Pagination
from pydantic import Field
from pydantic.networks import EmailStr
from pydantic.types import PositiveInt, condecimal
from utils.errors import OptionalNumbersError


class GenderEnum(str, Enum):
    male = "male"
    female = "female"
    other = "other"
    not_given = "not_given"


class PointContract:
    x: int = Field(..., description="X coordenates",
                   example="1", alias="x_coord")
    y: int = Field(..., description="Y coordenates",
                   example="2", alias="y_coord")

    class Config:
        title = "Point Model"
        orm_mode = True

        
class ExampleClassRequest:
    """Represents a Resquest to create an Example Endpoint"""

    name: str = Field(..., max_length=256, description="User name",
                      example="John Lennon", alias="name")

    gender: GenderEnum = Field(...,
                               description="Enumerator Class Model", alias="gender")
    email: EmailStr = Field(alias="email", description="User Email", example="john.lennon@gmail.com"
                            )
    float_number: Decimal = Field(
        ..., multiple_of=0.01, description="A float Number", example="1.11", alias="float_number"
    )
    optional_integer: Optional[PositiveInt] = Field(
        None, description="An optional positive integer", example="11", alias="optional_integer"
    )
    optional_float: Optional[condecimal(max_digits=18, decimal_places=2)] = Field(
        None, description="An optional float", example="1.12", alias="optional_float"
    )
    point: PointContract = Field(..., alias="point",
                                   description="example of relationship model. Set X and Y")
    

    class Config:
        title = "Exemple Model Creation"
        orm_mode = True

    # @pydantic.root_validator(pre=True)
    # @classmethod
    # def optional_numbers_must_be_null(cls, values):
    #     if ("optional_integer" and "optional_float") not in values:
    #         raise OptionalNumbersError(
    #             title=values["title"], message="Model must have one optional value"
    #         )

    @pydantic.validator('email')
    @classmethod
    def email_must_contains_at(cls, values):
        if "@" not in values:
            raise OptionalNumbersError(
                title=values["title"], message="Model must have one optional value"
            )


class DBExampleClass(DateTimeModelMixin, IDModelMixin, ExampleClassRequest):
    """Represents an Example Model in Database"""

    public_key: Union[int, str, uuid.UUID] = Field(..., alias="public key",
                                                   description="String identification",
                                                   example=uuid.uuid4()
                                                   )


class ExampleGetRespose(Pagination):
    example: DBExampleClass


# class ExampleResponse:
#     example: DBExampleClass
