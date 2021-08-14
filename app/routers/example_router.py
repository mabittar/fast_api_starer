from fastapi import APIRouter, Request, Response
from ..orm.example_model import BaseClassExample


example_endpoint = APIRouter()
controller = ExampleController()


@example_endpoint.post(
    "/example_post",
    response_model=BaseClassExample,
    status_code=201,
    tags=['basic example endpoint']
)
async def example_endpoint(req: Request, payload) -> Response:
    '''
    This is a endpoint to user BaseClassExample

    '''
    
    return await controller.create_example(payload)
