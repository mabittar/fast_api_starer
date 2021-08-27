from typing import Optional

from controller.example_controller import ExampleController
from sqlalchemy.orm.session import Session
from schemas import ExampleResponse, ExamplePaginatedResponse, ExampleClassRequest
from models.example_model import Example
from utils.logger import Logger


class ExampleService:
    def __init__(
        self,

        session: Session,
        logger: Optional[Logger] = None,
    ):
        self.logger = logger if logger is not None else Logger(class_name=__name__)
        self.session = session

    def get_data(
        self,
        example_data: Example,
        page: Optional[int] = None, 
        max_pagination: Optional[int] = None,
        first_result: Optional[bool] = False
    ):
        example_controller = ExampleController(session=self.session)
        if self.example_data.get("first_result"):
            example_data_model = example_controller.get(
                **example_data, first_result=first_result
            )

        elif page and max_pagination:
            example_data_model = example_controller.get(
                **example_data, page_number=page, page_size=max_pagination
            )
        else:
            example_data_model = example_controller.get(**example_data)

        # if example_data_model.optional_float and example_data_model.optional_integer:
        #     output_optional = example_data_model.optional_float * \
        #         example_data_model.optional_integer
        #     example_data_model.output_optional = output_optional

        return example_data_model

    def create_example(self, *, example_data: ExampleClassRequest):
        example_controller = ExampleController(session=self.session)
        example_data_model = example_controller.create(
            data=example_data)


        if example_data_model.optional_float and example_data_model.optional_integer:
            output_optional = example_data_model.optional_float * \
                example_data_model.optional_integer
            example_data_model.output_optional = output_optional


        return example_data_model

    def update_example(self, example_id, example_data: Example):
        example_controller = ExampleController(session=self.session)

        example_data_model_to_update = example_controller.get(
            example_id, first_result=True
        )

        example_data_model = example_controller.update(
            model=example_data_model_to_update, data=example_data
        )
        
        self.session.commit()
        return example_data_model

    def get_data_by_id(
        self,
        example_id,
    ):
        example_controller = ExampleController(session=self.session)
        example_data_model = example_controller.get(example_id=example_id)

        return example_data_model
