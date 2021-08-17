from datetime import datetime
from typing import List, Optional, Union

from controller.base_controller import BaseController
from orm.example_model import ExampleClassModel
from pydantic.types import UUID4


class ExampleController(BaseController):
    def __init__(self, session):
        self.session = session

    def create(self, data) -> ExampleClassModel:

        self.model = ExampleClassModel(**data)

        self.model.created_at = datetime.datetime.now()
        self.session.add(self.model)
        self.session.flush()

        return self.model

    def update(
        self,
        model: ExampleClassModel,
        public_key: Optional[UUID4],
        email: Optional[str],
        name: Optional[str],
        float_number: Optional[float],
        optional_integer: Optional[int],
        optional_float: Optional[float],
        domains: Optional[dict],
    ) -> ExampleClassModel:

        self.model = model
        if public_key is not None:
            self.model.public_key = public_key
        if name is not None:
            self.model.name = name
        if email is not None:
            self.model.email = email
        if float_number is not None:
            self.model.float_number = float_number
        if optional_float is not None:
            self.model.optional_float = optional_float
        if optional_integer is not None:
            self.model.optional_integer = optional_integer
        if domains is not None:
            self.model.domains = domains

        self.model.updated_at = datetime.datetime.now()

        self.session.add(self.model)
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
        page_number: Optional[int] = None,
        page_size: Optional[int] = None,
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

        if page_size and page_number:
            if order_by == "name_asc":
                query = query.order_by(__asc(ExampleClassModel.name))
            elif order_by == "name_desc":
                query = query.order_by(__desc(ExampleClassModel.name))
            elif order_by == "float_desc":
                query = query.order_by(__desc(ExampleClassModel.float_number))
            elif order_by == "float_asc":
                query = query.order_by(__asc(ExampleClassModel.float_number))
            elif order_by == "created_at_asc":
                query = query.order_by(__asc(ExampleClassModel.created_at))
            else:
                query = query.order_by(__desc(ExampleClassModel.created_at))
            query = query.limit(page_size).offset((page_number - 1) * page_size)

        result = query.first() if first_result else query.all()

        return result
