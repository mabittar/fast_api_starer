from typing import Optional

from controller.example_controller import ExampleController
from sqlalchemy.orm.session import Session
from controller.point_controller import PointController
from utils.logger import Logger


class ExampleService:
    def __init__(
        self,
        example_data: Optional[dict] = None,
        logger: Optional[Logger] = None,
        session: Optional[Session] = None,
    ):
        self.example_data = example_data
        self.logger = logger if logger is not None else Logger
        self.session = session if session is not None else Session

    def get_data(
        self, page: Optional[int] = None, max_pagination: Optional[int] = None
    ):
        example_controller = ExampleController(session=self.session)
        if self.example_data.get("first_result"):
            example_data_model = example_controller.get(
                **self.example_data, first_result=True
            )

        elif page and max_pagination:
            example_data_model = example_controller.get(
                **self.example_data, page_number=page, page_size=max_pagination
            )
        else:
            example_data_model = example_controller.get(**self.example_data)

        example_data_model.output_optional = (
            example_data_model.optional_integer / example_data_model.optional_float
        )

        return example_data_model.json()

    def create_example(self):
        point_controller = PointController(session=self.session)
        point_data = self.example_data.point
        point_model = point_controller.create(point_data)
        self.example_data.point = point_model
        example_controller = ExampleController(session=self.session)
        example_data_model = example_controller.create(self.example_data)
        self.session.commit()

        example_data_model.output_optional = (
            example_data_model.optional_integer / example_data_model.optional_float
        )

        return example_data_model.json()

    def update_example(self):
        point_controller = PointController(session=self.session)
        point_data = self.example_data.get("point")
        point_model = point_controller.create(**point_data)
        self.example_data.point = point_model
        example_controller = ExampleController(session=self.session)

        example_data_model_to_update = example_controller.get(
            **self.example_data, first_result=True
        )

        example_data_model = example_controller.update(
            model=example_data_model_to_update, **self.example_data
        )
        self.session.commit()

        example_data_model.output_optional = (
            example_data_model.optional_integer / example_data_model.optional_float
        )
        return example_data_model.json()
