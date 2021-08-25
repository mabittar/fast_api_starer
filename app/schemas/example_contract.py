import uuid
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Union

import pydantic
from pydantic.main import BaseModel
from common import DateTimeModelMixin, IDModelMixin, Pagination
from pydantic import Field
from pydantic.networks import EmailStr
from pydantic.types import PositiveInt, condecimal
from utils.errors import EmailMustContainsAt, OptionalNumbersError
import fastapi.utils as u


class GenderEnum(str, Enum):
    male = "male"
    female = "female"
    other = "other"
    not_given = "not_given"


class PointContract(BaseModel):
    x: int
    y: int


class PointInDB(IDModelMixin):
    pass 

    class Config:
        title = "Point Model"
        orm_mode = True

        
class ExampleClassRequest(BaseModel):
    """Represents a Resquest to create an Example after POST to Endpoint"""

    name: str
    gender: GenderEnum
    email: EmailStr
    float_number: Decimal
    optional_integer: int = None
    optional_float: Optional[condecimal(max_digits=18, decimal_places=2)] = None
    point: PointContract 

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

    public_key: Union[int, str, uuid.UUID]

    class config:
        orm_model = True
    

class ExampleGetRespose(Pagination, ExampleInDB):
    """Represents an Example Model to return via API"""
    pass


class ExampleResponse(ExampleInDB):
    """Represents an Example Model to return via API after GET"""
    pass
