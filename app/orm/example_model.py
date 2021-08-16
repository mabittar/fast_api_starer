from datetime import datetime
from decimal import Decimal
from typing import Union
import uuid
from pydantic import BaseModel, Field
from pydantic.networks import EmailStr
import pydantic
from utils.errors import OptionalNumbersError

class ExampleClassModel(BaseModel):
    '''Represents a basic model'''
    id: int = Field(int)
    public_key: Union[int, str, uuid.UUID] = Field(default_factory=uuid.uuid4,
                            description="String identification", example="UUID4")
    name: str = Field(str, description="User name", example="John Lennon")
    email: str = Field(EmailStr, max_length=200, description="User Email", example="john@beatles.com")
    float_number: float = Field(
        Decimal(), multiple_of=0.01, description="A float Number", example="1.1")
    optional_integer: int = Field(
        Decimal(), description="An optional integer", example="11")
    optional_float: float = Field(
        Decimal(), description="An optional float", example="0.12")
    updated_at: datetime = Field()
    created_at: datetime = Field(
        default_factory=datetime.now)
    # domains: list = Field(list)


    @pydantic.root_validator(pre=True)
    @classmethod
    def optional_numbers_must_be_null(cls, values):
        if ("optional_integer" and "optional_float") not in values:
            raise OptionalNumbersError(
                title=values["title"],
                message="Model must have one optional value"
            )
        
