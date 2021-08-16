from typing import List, Union
from services.example_service import ExampleService
from fastapi import APIRouter, Request, Response, HTTPException, Header
from orm.example_model import ExampleClassModel


example_router = APIRouter()
example_service = ExampleService()


@example_router.get(
    "/example",
    status_code=200,
    description="Use HTTPVerb GET to get example models",
    tags=['example model']
)
async def get_example_models(req: Request, internal_token: str = Header(...)) -> Response:
    '''
    This is a endpoint is used to get Example Class Model

    '''
    if internal_token != "example_secret_token":
        raise HTTPException(
            status_code=400, detail="Oops! Internal Token on header is invalid.")
    payload = req.body()
    if payload is None:
        raise HTTPException(status_code=404, detail=f"Oops! Payload cannot be null, please check documentation.")
    
    return await example_service.get_data(payload)


@example_router.post(
    "/example",
    status_code=201,
    description="Use HTTPVerb POST to create example model",
    tags=['example model']
)
async def create_example_model(req: Request) -> Response:
    '''
    This is a endpoint is used to post new Example Class Model

    '''
    payload = req.body()
    if payload is None:
        raise HTTPException(
            status_code=404, detail=f"Oops! Payload cannot be null, please check documentation.")
    
    response = example_service.create_example(payload)
    
    return await response
