from typing import Any, List, Optional, Union

from fastapi import APIRouter, HTTPException
from fastapi.params import Depends, Path
from sqlalchemy.orm.session import Session
import models
import schemas
from services.example_service import ExampleService
from utils.db.session import get_db

example_router = APIRouter()


@example_router.get(
    "/example",
    status_code=200,
    tags=["example model"],
    name='example:get example',
    response_model=Union[List[schemas.ExamplePaginatedResponse], schemas.ExamplePaginatedResponse],
    description="Use HTTP Method GET to get example models",
)
async def get_example_models(
    example_item,
    session: Session = Depends(get_db),
    page: Optional[int] = 1,
    max_pagination: Optional[int] = 10,
    first_result: Optional[bool] = False,
) -> Any:
    """
    This is a endpoint is used to get Example Class Model

    """

    if example_item is None:
        raise HTTPException(
            status_code=404,
            detail=f"Oops! Payload cannot be null, please check documentation.",
        )

    example_service = ExampleService(
        session=session)
    example_model = example_service.get_data(
        example_item, page, max_pagination, first_result)

    return await example_model


@example_router.get(
    "/example/{example_id}",
    status_code=200,
    tags=["example model"],
    name='example:get example by ID',
    response_model=schemas.ExampleResponse,
    description="Use HTTP Method GET to get example by ID",
)
async def get_example_by_id(
    example_id: int = Path(..., title="Use ID to get an example"),
    session: Session = Depends(get_db),
) -> Any:
    """
    This is a endpoint is used to get Example Class Model

    """

    if example_id is None:
        raise HTTPException(
            status_code=404,
            detail=f"Oops! ID cannot be null, please check documentation.",
        )

    example_service = ExampleService(
        session=session)
    example_model = example_service.get_data_by_id(
        example_id)

    return await example_model


@example_router.post(
    "/example",
    status_code=201,
    response_model=schemas.ExampleInDB,
    name='example:post create new example',
    response_model_exclude_unset=True,
    description="Use HTTP Method POST to create example model",
    tags=["example model"],
)
async def create_example_model(
        example_item: schemas.ExampleClassRequest,
        session: Session = Depends(get_db)
        ) -> Any:
    """
    This is a endpoint is used to create a new Example Class Model

    """
    
    if example_item is None:
        raise HTTPException(
            status_code=404,
            detail=f"Oops! Payload cannot be null, please check documentation.",
        )
 
    example_service = ExampleService(
        session=session)
    example_model = example_service.create_example(
        example_data=example_item)

    return example_model


@example_router.patch(
    "/example/{example_id}",
    status_code=200,
    response_model=schemas.ExampleInDB,
    name='example:patch to update an example',
    description="Use HTTP Method PATCH to update example model",
    tags=["example model"],
)
async def update_example_model(
        example_item: schemas.ExampleClassRequest,
        example_id: int = Path(..., title="Use ID to get an example"),
        session: Session = Depends(get_db)
        ):
    """
    This is a endpoint is used to update an existing Example Class Model

    """
    if example_item is None:
        raise HTTPException(
            status_code=404,
            detail=f"Oops! Payload cannot be null, please check documentation.",
        )
    example_service = ExampleService(
        session=session)
    model_updated = example_service.update_example(
        example_id, example_item)

    return model_updated
