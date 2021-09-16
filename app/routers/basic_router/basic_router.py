
from typing import List
import sys
from env_config import settings
from fastapi import APIRouter, Request
from starlette.responses import Response

router = APIRouter()

@router.get(
    "/",
    status_code=200,
    tags=["status"],
    description="Give some information about the running service",
)

async def home(req: Request):
    version = f"{sys.version_info.major}.{sys.version_info.minor}"
    message = f"Welcome to FaseAPI Starter! From Uvicorn with Gunicorn. Using Python {version}".encode(
        "utf-8"
    )
    response = dict(
        api=settings.PROJECT_NAME,
        msg=message
    )
    return response


@router.get(
    "/status",
    status_code=200,
    tags=["status"],
    description="Status Check",
)
async def health_check(req: Request):
    return Response(status_code=200)


@router.get(
    "/status/all_routes", 
    tags=["status"], 
    description="List all available routes"
)
async def get_all_routes(req: Request) -> List[str]:
    # Using FastAPI instance
    url_list = [{"path": route.path, "name": route.name} for route in req.app.routes]
    return url_list
