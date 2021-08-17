from typing import Optional

from utils.database import DBConnector
from .contract.example_contract import ExampleClassRequest, ExampleClassResponse
from services.example_service import ExampleService
from fastapi import APIRouter, HTTPException, Request


example_router = APIRouter()


@example_router.get(
    "/example",
    status_code=200,
    tags=['example model'],
    response_model=ExampleClassResponse,
    description="Use HTTPVerb GET to get example models",
)
async def get_example_models(
    example_item: ExampleClassRequest, 
    page: Optional[int] = 1,
    max_pagination: Optional[int] = 10,
    ):
    '''
    This is a endpoint is used to get Example Class Model

    '''
    # if internal_token != "example_secret_token":
    #     raise HTTPException(
    #         status_code=400, detail="Oops! Internal Token on header is invalid.")

    if example_item is None:
        raise HTTPException(status_code=404, detail=f"Oops! Payload cannot be null, please check documentation.")
    with DBConnector.session_scope() as session:
        example_service = ExampleService(session=session)
        example_model = example_service.get_data(
            example_item, page, max_pagination)

        return await example_model


@example_router.post(
    "/example",
    status_code=201,
    response_model=ExampleClassResponse,
    description="Use HTTPVerb POST to create example model",
    tags=['example model']
)
async def create_example_model(
    req: Request, 
    example_item: ExampleClassRequest):
    '''
    This is a endpoint is used to post new Example Class Model

    '''
    if example_item is None:
        raise HTTPException(
            status_code=404, detail=f"Oops! Payload cannot be null, please check documentation.")
    with DBConnector.session_scope() as session:
        example_service = ExampleService(session=session)
        new_item_model = example_service.create_example(example_item)

        return await new_item_model


@example_router.patch(
    "/example",
    status_code=200,
    response_model=ExampleClassResponse,
    description="Use HTTPVerb PATCH to update example model",
    tags=['example model']
)
async def update_example_model(example_item: ExampleClassRequest):
    '''
    This is a endpoint is used to update an existing Example Class Model

    '''
    if example_item is None:
        raise HTTPException(
            status_code=404, detail=f"Oops! Payload cannot be null, please check documentation.")
    with DBConnector.session_scope() as session:
        example_service = ExampleService(session=session)
        model_updated = example_service.update_example(example_item)

        return await model_updated
