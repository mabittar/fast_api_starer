import uuid
from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import Optional, Union

import pydantic
from pydantic import BaseModel, Field
from pydantic.networks import EmailStr
from pydantic.types import PositiveInt, condecimal, conint
from utils.errors import OptionalNumbersError


class Gender(str, Enum):
    male = "male"
    female = "female"
    other = ("other",)
    not_given = "not_given"


class ExampleClassRequest(BaseModel):
    """Represents a basic model"""

    id: int
    public_key: Union[int, str, uuid.UUID] = Field(
        default_factory=lambda: uuid.uuid4().hex,
        alias="public key",
        description="String identification",
        example=uuid.uuid4(),
    )
    name: str = Field(
        ..., alias="User Name", description="User name", example="John Lennon"
    )
    gender: Gender = Field(..., alias="Gender")
    email: EmailStr = Field(
        ..., alias="user email", description="User Email", example="john@beatles.com"
    )
    float_number: condecimal    (max_digits=18, decimal_places=2) = Field(
        ..., multiple_of=0.01, description="A float Number", example="1.11"
    )
    optional_integer: Optional[PositiveInt] = Field(
        None, description="An optional integer", example="11"
    )
    optional_float: Optional[condecimal(max_digits=18, decimal_places=2)] = Field(
        None, description="An optional float", example="0.12"
    )
    updated_at: Optional[datetime] = None
    created_at: datetime = Field(default_factory=datetime.now)
    page: Optional[conint(ge=1, le=999)] = 1
    max_pagination: Optional[conint(ge=1, le=999)] = 100

    class Config:
        title = "Exemple Model"
        orm_mode = True

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
            raise OptionalNumbersError(
                title=values["title"], message="Model must have one optional value"
            )


class ExampleClassResponse(BaseModel):
    """Represents a basic model"""

    id: int
    public_key: Union[int, str, uuid.UUID]
    name: str
    gender: Gender
    email: str
    float_number: condecimal(max_digits=18, decimal_places=2)
    optional_integer: Optional[PositiveInt]
    optional_float: Optional[condecimal(max_digits=18, decimal_places=2)]
    output_optional: Optional[condecimal(
        max_digits=18, decimal_places=2)]
    updated_at: Optional[datetime]
    created_at: datetime
    page: Optional[int]
    max_pagination: Optional[int]
