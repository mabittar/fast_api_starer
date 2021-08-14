from starlette.responses import Response
from utils.config import PROJECT_NAME
from os import getpid
from typing import List
from fastapi import APIRouter, Request
from enum import Enum
from pydantic import BaseModel, Field


class StatusResponse(BaseModel):
    api: str = Field(..., description="API Name", example="entrance")
    id: int = Field(..., description="Interface Id", example=123456)

router = APIRouter()


@router.get(
    "/",
    status_code=200,
    tags=["status"],
    response_model=StatusResponse,
    description="Give some information about the running service",
)
async def home(req: Request) -> StatusResponse:
    return StatusResponse(
        service=PROJECT_NAME, id=getpid()
    )


@router.get(
    "/status",
    status_code=200,
    tags=["status"],
    description="Status Check",
)
async def health_check(req: Request) -> Response:
    return Response(status_code=200)


@router.get(
    "/status/all_routes", tags=["status"], description="List all available routes"
)
async def get_all_routes(req: Request) -> List[str]:
    # Using FastAPI instance
    url_list = [{"path": route.path, "name": route.name}
                for route in req.app.routes]
    return url_list
