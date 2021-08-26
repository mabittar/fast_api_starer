from datetime import datetime
from typing import List, Optional, Union
import uuid

from sqlalchemy.orm.session import Session
from sqlalchemy.sql.expression import asc, desc
from controller.base_controller import CRUDBase

from schemas.example_contract import ExampleClassRequest
from models.example_model import Example
from pydantic.types import UUID4

from utils.db.database import get_db


class ExampleController(CRUDBase):
    def __init__(self, session: Optional[Session] = None):
        super().__init__(model=Example)
        self.session = session if session else get_db()

    def create(self, data: ExampleClassRequest):
        model = Example(
            
            name=data.name,
            gender=data.gender,
            email=data.email,
            float_number=data.float_number,
            optional_integer=data.optional_integer,
            optional_float=data.optional_float

            )
        model.public_key = str(uuid.uuid4())
        self.session.add(model)
        self.session.flush()
        self.session.refresh(model)

        return model

    async def update(
        self,
        model: Example,

        data: Example
    ) -> Example:
        model = Example(**data.dict())
        model.updated_at = datetime.datetime.now()

        self.session.add(model)
        self.session.flush()

        return self.model

    def get(
        self,
        example_id: Optional[int],
        public_key: Optional[UUID4],
        name: Optional[str],
        float_number: Optional[float],
        optional_integer: Optional[int],
        optional_float: Optional[float],
        first_result: Optional[bool],
        page: Optional[int] = None,
        max_pagination: Optional[int] = None,
        order_by: Optional[str] = None,
    ) -> Union[List[Example], Example]:

        query = self.new_query(Example)

        if example_id is not None:
            query = query.filter(Example.id == example_id)

        if public_key is not None:
            query = query.filter(Example.public_key == public_key)

        if name is not None:
            query = query.filter(Example.name == name)

        if float_number is not None:
            query = query.filter(Example.float_number == float_number)

        if optional_integer is not None:
            query = query.filter(Example.optional_integer == optional_integer)

        if optional_float is not None:
            query = query.filter(Example.optional_float == optional_float)

        if page and max_pagination:
            if order_by == "name_asc":
                query = query.order_by(asc(Example.name))
            elif order_by == "name_desc":
                query = query.order_by(desc(Example.name))
            elif order_by == "float_desc":
                query = query.order_by(asc(Example.float_number))
            elif order_by == "float_asc":
                query = query.order_by(desc(Example.float_number))
            elif order_by == "created_at_asc":
                query = query.order_by(desc(Example.created_at))
            else:
                query = query.order_by(desc(Example.created_at))
            query = query.limit(max_pagination).offset(
                (page - 1) * max_pagination)

        result = query.first() if first_result else query.all()

        return result
