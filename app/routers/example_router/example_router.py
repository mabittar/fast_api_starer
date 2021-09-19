from typing import Any, List, Optional, Union
from sqlalchemy.future import select
from fastapi import APIRouter, HTTPException
from fastapi.params import Depends, Path
from sqlalchemy.ext.asyncio.session import AsyncSession
from models.example_model import Example, ExampleCreate, ExampleGet, ExampleUpdate
from services.example_service import ExampleService
from utils.db.database import SQLConnector

example_router = APIRouter()

@example_router.get(
    "/example",
    status_code=200,
    tags=["example model"],
    name='example:get example',
    response_model=Union[List[ExampleGet], ExampleGet],
    description="Use HTTP Method GET to get example models",
)
async def get_examples(
    page: Optional[int] = 1,
    max_pagination: Optional[int] = 10,
    first_result: Optional[bool] = False,
    session: AsyncSession = Depends(SQLConnector.get_session)
) -> Any:
    """
    This is a endpoint is used to get Example Class Model

    """
    example_service = ExampleService(session=session)
    results = await example_service.get_data(ExampleGet, page=page, max_pagination=max_pagination, first_result=first_result)
    
    response = [ExampleGet(
        name=example.name, 
        email=example.email,
        gender=example.gender,
        float_number=example.float_number,
        optional_integer=example.optional_integer,
        optional_float=example.optional_float,
        id=example.id,
        public_key=example.public_key,
        created_at=example.created_at,
    ) for example in results]

    return response

@example_router.post(
    "/example",
    status_code=201,
    response_model=ExampleCreate,
    name='example:post create new example',
    description="Use HTTP Method POST to create example model",
    tags=["example model"],
)
async def add_example(
        example_item: ExampleCreate,
        session: AsyncSession = Depends(SQLConnector.get_session)
        ) -> Any:
    """
    This is a endpoint is used to create a new Example Class Model

    """
    
    if example_item is None:
        raise HTTPException(
            status_code=404,
            detail=f"Oops! Payload cannot be null, please check documentation.",
        )

    
    example_service = ExampleService(session=session)
    example = await example_service.create_example(example_item)
    
    await session.commit()
    await session.refresh(example)
    
    return example


@example_router.patch(
    "/example/{example_id}",
    status_code=200,
    response_model=ExampleUpdate,
    name='example:patch to update an example',
    description="Use HTTP Method PATCH to update example model",
    tags=["example model"],
)
async def update_example_model(
        example_item: ExampleCreate,
        example_id: int = Path(..., title="Use ID to get an example"),
        session: AsyncSession = Depends(SQLConnector.get_session)
        ):
    """
    This is a endpoint is used to update an existing Example Class Model

    """
    if example_item is None:
        raise HTTPException(
            status_code=404,
            detail=f"Oops! Payload cannot be null, please check documentation.",
        )

    with SQLConnector.create_session() as session:
        example_service = ExampleService(
            session=session)
        model_updated = example_service.update_example(
            example_id, example_item)

        return model_updated
