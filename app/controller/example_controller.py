

from datetime import datetime
from typing import List, Optional, Union

from pydantic.types import UUID4
from app.orm.example_model import BaseClassExample
from ..controller.base_controller import BaseController


class ExampleController(BaseController):
    def __init__(self, session):
        self.session = session

    def create(
        self,
        public_key,
        name,
        float_number,
        optional_integer,
        optional_float,
        domains
    ) -> BaseClassExample:

        self.model = BaseClassExample()
        self.model.public_key = public_key
        self.model.name = name
        self.model.float_number = float_number
        self.model.optional_integer = optional_integer
        self.model.optional_float = optional_float
        self.model.domains = domains

        self.model.created_at = datetime.datetime.now()
        self.session.add(self.model)

        return self.model

    def update(
        self,
        model: BaseClassExample,
        public_key: Optional[UUID4],
        name: Optional[str],
        float_number: Optional[float],
        optional_integer: Optional[int],
        optional_float: Optional[float],
        domains: Optional[dict]
    ) -> BaseClassExample:

        self.model = model
        if public_key is not None:
            self.model.public_key = public_key
        if name is not None:
            self.model.name = name
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

        
    ) -> Union[List[BaseClassExample], BaseClassExample]:

        query = self.new_query(BaseClassExample)
        
        if example_id is not None:
            query = query.filter(BaseClassExample.id == example_id)

        if public_key is not None:
            query = query.filter(BaseClassExample.public_key == public_key)

        if name is not None:
            query = query.filter(BaseClassExample.name == name)

        if float_number is not None:
            query = query.filter(BaseClassExample.float_number == float_number)

        if optional_integer is not None:
            query = query.filter(BaseClassExample.optional_integer == optional_integer)

        if optional_float is not None:
            query = query.filter(BaseClassExample.optional_float == optional_float)

        if page_size and page_number:
            if order_by == "name_asc":
                query = query.order_by(__asc(BaseClassExample.name))
            elif order_by == "name_desc":
                query = query.order_by(__desc(BaseClassExample.name))
            elif order_by == "float_desc":
                query = query.order_by(
                    __desc(BaseClassExample.float_number))
            elif order_by == "float_asc":
                query = query.order_by(
                    __asc(BaseClassExample.float_number))
            elif order_by == "created_at_asc":
                query = query.order_by(__asc(BaseClassExample.created_at))
            else:
                query = query.order_by(__desc(BaseClassExample.created_at))
            query = query.limit(page_size).offset(
                (page_number - 1) * page_size)


        result = query.first() if first_result else query.all()

        return result
