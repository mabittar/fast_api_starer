from .contract.status_contract import StatusResponseModel
from starlette.responses import Response
from env_config import settings
from os import getpid
from typing import List
from fastapi import APIRouter, Request




router = APIRouter()


@router.get(
    "/",
    status_code=200,
    tags=["status"],
    response_model=StatusResponseModel,
    description="Give some information about the running service",
)
async def home(req: Request) -> StatusResponseModel:
    return StatusResponseModel(
        service=settings.project_name, id=getpid()
    )


@router.get(
    "/status",
    status_code=200,
    tags=["status"],
    description="Status Check",
)
async def health_check(req: Request) -> StatusResponseModel:
    return Response(status_code=200)


@router.get(
    "/status/all_routes", tags=["status"], description="List all available routes"
)
async def get_all_routes(req: Request) -> List[str]:
    # Using FastAPI instance
    url_list = [{"path": route.path, "name": route.name}
                for route in req.app.routes]
    return url_list
