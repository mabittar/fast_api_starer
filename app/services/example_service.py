from pydantic.types import Json
from controller.example_controller import ExampleController
from sqlalchemy.orm.session import Session
from utils.logger import Logger
from typing import Optional
from utils.logger import Logger
from starlette.exceptions import HTTPException

class ExampleService:
    def __init__(self, example_data: Optional[dict] = None, logger: Optional[Logger] = None, session: Optional[Session] = None):
        self.example_data = example_data
        self.logger = logger if logger is not None else Logger
        self.session = session if session is not None else Session


    def get_data(self) -> Json:
        if self.example_data is None:
            raise HTTPException(
                status_code=400,
                detail="Example data can not be null."
            )
        
        example_controller = ExampleController(session=self.session)
        example_data_model = example_controller.get(**self.example_data)

        return example_data_model.json()

    def create_example(self):
        pass