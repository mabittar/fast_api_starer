from typing import Optional

from fastapi import APIRouter, HTTPException, Request
from fastapi.params import Path
from services.example_service import ExampleService
from utils.database import DBConnector

from model.contracts.example_contract import ExampleClassRequest, DBExampleClass

example_router = APIRouter()


@example_router.get(
    "/example",
    status_code=200,
    tags=["example model"],nam

    response_model=DBExampleClass,
    description="Use HTTPVerb GET to get example models",
)
async def get_example_models(
    example_item: ExampleClassRequest,
    page: Optional[int] = 1,
    max_pagination: Optional[int] = 10,
    first_result: Optional[bool] = False,
):
    """
    This is a endpoint is used to get Example Class Model

    """

    if example_item is None:
        raise HTTPException(
            status_code=404,
            detail=f"Oops! Payload cannot be null, please check documentation.",
        )
    with DBConnector.session_scope() as session:
        example_service = ExampleService(
            session=session, example_data=example_item)
        example_model = example_service.get_data(
            page, max_pagination, first_result)

        return await example_model


@example_router.get(
    "/example/{example_id}",
    status_code=200,
    tags=["example model"],
    response_model=DBExampleClass,
    description="Use HTTPVerb GET to get example by ID",
)
async def get_example_by_id(
    example_id:int = Path(..., title="Use ID to get an example")
):
    """
    This is a endpoint is used to get Example Class Model

    """

    if example_id is None:
        raise HTTPException(
            status_code=404,
            detail=f"Oops! ID cannot be null, please check documentation.",
        )
    with DBConnector.session_scope() as session:
        example_service = ExampleService(
            session=session)
        example_model = example_service.get_data_by_id(
            example_id)

        return await example_model


@example_router.post(
    "/example",
    status_code=201,
    response_model=DBExampleClass,
    response_model_exclude_unset=True,
    description="Use HTTPVerb POST to create example model",
    tags=["example model"],
)
async def create_example_model(req: Request, example_item: ExampleClassRequest):
    """
    This is a endpoint is used to post new Example Class Model

    """
    
    if example_item is None:
        raise HTTPException(
            status_code=404,
            detail=f"Oops! Payload cannot be null, please check documentation.",
        )
    with DBConnector.session_scope() as session:
        example_service = ExampleService(
            session=session, example_data=example_item)
        new_item_model = example_service.create_example()

        return new_item_model


@example_router.patch(
    "/example/{example_id}",
    status_code=200,
    response_model=DBExampleClass,
    description="Use HTTPVerb PATCH to update example model",
    tags=["example model"],
)
async def update_example_model(
    example_item: ExampleClassRequest,
    example_id: int = Path(..., title="Use ID to get an example"), ):
    """
    This is a endpoint is used to update an existing Example Class Model

    """
    if example_item is None:
        raise HTTPException(
            status_code=404,
            detail=f"Oops! Payload cannot be null, please check documentation.",
        )
    with DBConnector.session_scope() as session:
        example_service = ExampleService(
            session=session, example_data=example_item)
        model_updated = example_service.update_example(example_id)

        return await model_updated
