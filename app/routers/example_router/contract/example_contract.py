import uuid
from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import Optional, Union

import pydantic
from pydantic import BaseModel, Field
from pydantic.networks import EmailStr
from pydantic.types import PositiveInt
from utils.errors import OptionalNumbersError


class Gender(str, Enum):
    male = 'male'
    female = 'female'
    other = 'other',
    not_given = 'not_given'


class ExampleClassRequest(BaseModel):
    '''Represents a basic model'''
    id: int
    public_key: Union[int, str, uuid.UUID] = Field(default_factory=lambda: uuid.uuid4().hex, alias='public key',
                                                   description="String identification", example=uuid.uuid4())
    name: str = Field(..., alias="User Name",
                      description="User name", example="John Lennon")
    gender: Gender = Field(..., alias='Gender')
    email: EmailStr = Field(..., alias='user email',
                       description="User Email", example="john@beatles.com")
    float_number: Decimal = Field(
        ..., multiple_of=0.01, description="A float Number", example="1.1")
    optional_integer: Optional[PositiveInt] = Field(
        None, description="An optional integer", example="11")
    optional_float: Optional[Decimal] = Field(
        None, description="An optional float", example="0.12")
    updated_at: Optional[datetime] = None
    created_at: datetime = Field(
        default_factory=datetime.now)

    class Config:
        title = 'Exemple Model'
        orm_mode = True

    @pydantic.root_validator(pre=True)
    @classmethod
    def optional_numbers_must_be_null(cls, values):
        if ("optional_integer" and "optional_float") not in values:
            raise OptionalNumbersError(
                title=values["title"],
                message="Model must have one optional value"
            )


class ExampleClassResponse(BaseModel):
    '''Represents a basic model'''
    id: int
    public_key: Union[int, str, uuid.UUID]
    name: str
    gender: Gender = Field(..., alias='Gender')
    email: str
    float_number: float
    optional_integer: Optional[PositiveInt] = 1
    optional_float: Optional[Decimal] = 0.0
    output_optional: Optional[Decimal] = None
    updated_at: Optional[datetime] = None
    created_at: datetime
    page: Optional[int] = 1
    max_pagination: Optional[int] = 10
