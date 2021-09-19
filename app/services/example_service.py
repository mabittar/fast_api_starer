from typing import Optional
from uuid import uuid4
from datetime import datetime
from sqlalchemy.future import select
from sqlmodel import Session

from controller.example_controller import ExampleController
from models.example_model import Example, ExampleCreate, ExampleGet
from utils.db.database import SQLConnector
from utils.logger import Logger


class ExampleService:
    def __init__(
        self,
        logger: Optional[Logger] = None,
        session: Session = None
    ):
        self.logger = logger if logger is not None else Logger(class_name=__name__)
        self.session = session if session is not None else SQLConnector.get_session
    
    async def get_data(
        self,
        example_data: ExampleGet,
        page: Optional[int] = 1, 
        max_pagination: Optional[int] = 15,
        first_result: Optional[bool] = False
    ):
        with self.session:
            query = select(ExampleGet)
            if id is not None:
                query = self.session.exec(query).where(ExampleGet.id == example_data.id)
            if first_result:
                query = self.session.exec(query).first()
                return query
            else:
                query = self.session.exec(query)

                if page and max_pagination:
                    query = self.session.exec(query).offset(
                        page * max_pagination).limit(max_pagination)

            return query

    async def create_example(self, example_data: Example):
        example = Example(
            name=example_data.name,
            email=example_data.email,
            gender=example_data.gender,
            float_number=example_data.float_number,
            optional_integer=example_data.optional_integer,
            optional_float=example_data.optional_float,
            public_key=uuid4(),
            created_at=datetime.now()
        )
        self.session.add(example)
        self.session.flush()

        return example

    def update_example(self, example_id, example_data: Example):
        example_controller = ExampleController(self.session)

        example_data_model_to_update = example_controller.get(
            example_id, first_result=True
        )

        example_data_model = example_controller.update(
            model=example_data_model_to_update, data=example_data
        )
        return example_data_model

    def get_data_by_id(
        self,
        example_id,
    ):
        example_controller = ExampleController()
        example_data_model = example_controller.get(example_id=example_id)

        return example_data_model
