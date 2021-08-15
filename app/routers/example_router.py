from starlette.responses import JSONResponse
from ..services.example_service import ExampleService
from fastapi import APIRouter, Request, Response
from ..orm.example_model import BaseClassExample


example_endpoint = APIRouter()
controller = ExampleService()


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


@example_endpoint.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=400,
        content={
            "message": f"Oops! {exc.name} some thing goes wrong, pleas check documentation."},
    )

@example_endpoint.get(
    "/example_get",
    response_model=BaseClassExample,
    status_code=201,
    tags=['basic example endpoint']
)
async def example_endpoint(req: Request, payload) -> Response:
    '''
    This is a endpoint to get BaseClassExample

    '''
    if payload is None:
        raise UnicornException
    
    return await controller.get_data(payload)


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
    if payload is None:
        raise UnicornException
    
    return await controller.create_example(payload)
