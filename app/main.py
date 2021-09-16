import sys

from env_config import settings
from fastapi import FastAPI
from fastapi_load import FastAPIStarter
from middlewares import custom_middlewares_list
from routers import routers_list
from utils.logger import Logger

version = f"{sys.version_info.major}.{sys.version_info.minor}"


class App:
    async def on_startup(self):
        Logger(class_name=__name__).info(
            msg=f"{settings.PROJECT_NAME} STARTING...Using python version {version} and Uvicorn with Gunicorn"
        )

    async def on_shutdown(self):
        Logger(class_name=__name__).info(
            msg=f"{settings.PROJECT_NAME} STOPING API..."
        )

    # add new endpoints to init routers_list
    # add new middlewares to init middlewares
    def create(self) -> FastAPI:
        api = FastAPIStarter.start_up(
            title="FastAPI Fast Starter Project",
            routers=routers_list,
            middlewares=custom_middlewares_list,
            on_startup=[self.on_startup],
            on_shutdown=[self.on_shutdown],
        )

        return api


app = App().create()
