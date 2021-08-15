from utils.database import DBConnector
from utils.logger import Logger
from fastapi_load import FastAPIStarter
from fastapi import FastAPI
from env_config import settings
import sys

version = f"{sys.version_info.major}.{sys.version_info.minor}"


class App:

    async def on_startup(self):
        DBConnector.create_engine()
        Logger().info(msg=f"{settings.project_name} STARTING...Using python version {version} and Uvicorn with Gunicorn")


    async def on_shutdown(self):
        DBConnector.close()
        Logger.info(msg="shutting down...")

    # add middlewares using create attr
    def create(self) -> FastAPI:
        api = FastAPIStarter.create(
            title="FastAPI Fast Starter Project",
            on_startup=[self.on_startup],
            on_shutdown=[self.on_shutdown],
        )

        return api


app = App().create()



