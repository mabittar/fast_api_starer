from datetime import datetime
from typing import List, Optional, Union
import uuid

from sqlalchemy.orm.session import Session
from sqlalchemy.sql.expression import asc, desc
from controller.base_controller import CRUDBase

from model.contracts.example_contract import ExampleClassRequest
from orm.example_model import ExampleClassModel
from pydantic.types import UUID4

from utils.database import get_db


class ExampleController(CRUDBase):
    def __init__(self, session: Optional[Session] = None):
        super().__init__(model=ExampleClassModel)
        self.session = session if session else get_db()

    def create(self, data: ExampleClassRequest):
        model = ExampleClassModel(**data.dict())
        model.public_key = str(uuid.uuid4())
        model.created_at = datetime.datetime.now()
        self.session.add(model)
        self.session.flush()
        self.session.commit()
        self.session.refresh(model)

        return model

    async def update(
        self,
        model: ExampleClassModel,

        data: ExampleClassModel
    ) -> ExampleClassModel:
        model = ExampleClassModel(**data.dict())
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
    ) -> Union[List[ExampleClassModel], ExampleClassModel]:

        query = self.new_query(ExampleClassModel)

        if example_id is not None:
            query = query.filter(ExampleClassModel.id == example_id)

        if public_key is not None:
            query = query.filter(ExampleClassModel.public_key == public_key)

        if name is not None:
            query = query.filter(ExampleClassModel.name == name)

        if float_number is not None:
            query = query.filter(ExampleClassModel.float_number == float_number)

        if optional_integer is not None:
            query = query.filter(ExampleClassModel.optional_integer == optional_integer)

        if optional_float is not None:
            query = query.filter(ExampleClassModel.optional_float == optional_float)

        if page and max_pagination:
            if order_by == "name_asc":
                query = query.order_by(asc(ExampleClassModel.name))
            elif order_by == "name_desc":
                query = query.order_by(desc(ExampleClassModel.name))
            elif order_by == "float_desc":
                query = query.order_by(asc(ExampleClassModel.float_number))
            elif order_by == "float_asc":
                query = query.order_by(desc(ExampleClassModel.float_number))
            elif order_by == "created_at_asc":
                query = query.order_by(desc(ExampleClassModel.created_at))
            else:
                query = query.order_by(desc(ExampleClassModel.created_at))
            query = query.limit(max_pagination).offset(
                (page - 1) * max_pagination)

        result = query.first() if first_result else query.all()

        return result
