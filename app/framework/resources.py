from starlette.responses import Response
from utils.config import COMMIT, SERVICE_NAME
from os import getpid
from typing import List
from fastapi import APIRouter, Request, responses
from enum import Enum
from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    service: str = Field(..., description="Service Name", example="proxy")
    commit: str = Field(..., description="Running commit", example="2c5d720")
    id: int = Field(..., description="Process Identification", example=123456)

router = APIRouter()


@router.get(
    "/",
    status_code=200,
    tags=["health"],
    response_model=HealthResponse,
    description="Give some information about the running service",
)
async def home(req: Request) -> HealthResponse:
    return HealthResponse(
        service=SERVICE_NAME, commit=COMMIT, id=getpid()
    )


@router.get(
    "/health_check",
    status_code=200,
    tags=["health"],
    description="Health Checks",
)
async def health_check(req: Request) -> Response:
    return Response(status_code=200)


@router.get(
    "/health_check/all_routes", tags=["health"], description="List all available routes"
)
async def get_all_routes(req: Request) -> List[str]:
    # Using FastAPI instance
    url_list = [{"path": route.path, "name": route.name}
                for route in req.app.routes]
    return url_list
