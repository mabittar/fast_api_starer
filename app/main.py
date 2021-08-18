import sys

from env_config import settings
from fastapi import FastAPI
from fastapi_load import FastAPIStarter
from utils.database import DBConnector
from utils.logger import Logger
from middleware import custom_middlewares_list
from routers.basic_router.basic_router import router
from routers.example_router.example_router import example_router

version = f"{sys.version_info.major}.{sys.version_info.minor}"


class App:
    async def on_startup(self):
        DBConnector.create_engine()
        Logger().info(
            msg=f"{settings.project_name} STARTING...Using python version {version} and Uvicorn with Gunicorn"
        )

    async def on_shutdown(self):
        DBConnector.close()
        Logger.info(msg="shutting down...")

    # add new endpoints to routers
    def create(self) -> FastAPI:
        api = FastAPIStarter.start_up(
            title="FastAPI Fast Starter Project",
            routers=[router, example_router],
            middlewares=custom_middlewares_list,
            on_startup=[self.on_startup],
            on_shutdown=[self.on_shutdown],
        )

        return api


app = App().create()
