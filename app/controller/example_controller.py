from datetime import datetime
from typing import List, Optional, Union
import uuid

from sqlalchemy.orm.session import Session

from controller.base_controller import CRUDController
from model.contracts.example_contract import ExampleClassRequest
from orm.example_model import ExampleClassModel
from pydantic.types import UUID4



class ExampleController(CRUDController):
    def __init__(self, session: Session) -> None:
        super().__init__(model=ExampleClassModel)
        self.session = session

    def create(self, data: ExampleClassRequest):
        model = ExampleClassModel(
            name=data.name,
            gender=data.gender,
            email=data.email,
            float_number=data.float_number,
            optional_integer=data.optional_integer,
            optional_float=data.optional_float,
            point=data.point
        )
        model.public_key = str(uuid.uuid4())
        model.created_at = datetime.datetime.now()
        self.session.add(model)
        self.session.flush()

        return model

    async def update(
        self,
        model: ExampleClassModel,

        data: ExampleClassModel
    ) -> ExampleClassModel:
        model = ExampleClassModel(
            name=data.name,
            gender=data.gender,
            email=data.email,
            float_number=data.float_number,
            optional_integer=data.optional_integer,
            optional_float=data.optional_float,
            point=data.point
        )
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
