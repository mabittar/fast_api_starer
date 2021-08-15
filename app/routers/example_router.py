from typing import List, Union
from starlette.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from services.example_service import ExampleService
from fastapi import APIRouter, Request, Response, HTTPException
from orm.example_model import ExampleClassModel


example_router = APIRouter()
example_service = ExampleService()

@example_router.get(
    "/example_get",
    response_model=Union[List[ExampleClassModel],
                         ExampleClassModel],
    status_code=200,
    tags=['basic example endpoint']
)
async def example_router(req: Request) -> Response:
    '''
    This is a endpoint to get BaseClassExample

    '''
    payload = req.body()
    if payload is None:
        raise HTTPException(status_code=404, detail=f"Oops! Payload cannot be null, please check documentation.")
    
    return await example_service.get_data(payload)


@example_router.post(
    "/example_post",
    response_model=ExampleClassModel,
    status_code=201,
    tags=['basic example endpoint']
)
async def example_router(req: Request) -> Response:
    '''
    This is a endpoint to user BaseClassExample

    '''
    payload = req.body()
    if payload is None:
        raise HTTPException(
            status_code=404, detail=f"Oops! Payload cannot be null, please check documentation.")
    
    response = example_service.create_example(payload)
    
    return await response
