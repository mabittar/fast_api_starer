import uuid
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Union

import pydantic
from pydantic.main import BaseModel
from .common import DateTimeModelMixin, IDModelMixin, Pagination
from pydantic import Field
from pydantic.networks import EmailStr
from pydantic.types import PositiveInt, condecimal
from utils.errors import EmailMustContainsAt, OptionalNumbersError


class GenderEnum(str, Enum):
    male = "male"
    female = "female"
    other = "other"
    not_given = "not_given"


class PointContract(BaseModel):
    x: int = Field(..., description="X coordenates",
                   example="1", alias="x_coord")
    y: int = Field(..., description="Y coordenates",
                   example="2", alias="y_coord")


class PointInDB(IDModelMixin):
    pass 

    class Config:
        title = "Point Model"
        orm_mode = True

        
class ExampleClassRequest(BaseModel):
    """Represents a Resquest to create an Example after POST to Endpoint"""

    name: str = Field(..., max_length=256, description="User name",
                      example="John Lennon", alias="name")
    gender: GenderEnum = Field(...,
                               description="Enumerator Class Model", alias="gender")
    email: EmailStr = Field(alias="email", description="User Email", example="john@beatles.com"
                            )
    float_number: Decimal = Field(
        ..., multiple_of=0.01, description="A float Number", example="1.11", alias="float_number"
    )
    optional_integer: int = Field(
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
        arbitrary_types_allowed = True

    @pydantic.root_validator(pre=True)
    @classmethod
    def optional_numbers_must_be_null(cls, values):
        if ("optional_integer" and "optional_float") not in values:
            raise OptionalNumbersError(
                title=values["title"], message="Model must have one optional value"
            )

    @pydantic.validator('email')
    @classmethod
    def email_must_contains_at(cls, values):
        if "@" not in values:
            raise EmailMustContainsAt(
                title=values["title"], message="Model must have one optional value"
            )


class ExampleInDB(DateTimeModelMixin, IDModelMixin, ExampleClassRequest):
    """Represents an Example Model in Database"""

    public_key: Union[int, str, uuid.UUID] = Field(..., alias="public key",
                                                   description="String identification",
                                                   example=uuid.uuid4()
                                                   )

    class config:
        orm_model = True
    

class ExampleGetRespose(Pagination, ExampleInDB):
    """Represents an Example Model to return via API"""
    pass


class ExampleResponse(ExampleInDB):
    """Represents an Example Model to return via API after GET"""
    pass
