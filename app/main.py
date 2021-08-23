import sys

from env_config import settings
from fastapi import FastAPI
from fastapi_load import FastAPIStarter
from utils.database import get_db
from utils.logger import Logger
from middlewares import custom_middlewares_list
from routers import routers_list
from utils.database import engine
from orm import models
version = f"{sys.version_info.major}.{sys.version_info.minor}"


class App:
    async def on_startup(self):
        get_db()
        Logger().info(
            msg=f"{settings.project_name} STARTING...Using python version {version} and Uvicorn with Gunicorn"
        )

    async def on_shutdown(self):
        get_db().close()
        Logger.info(msg="shutting down...")

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

if len(models) != 0:
    for model in models:
        model.Base.create_all(bind=engine)

app = App().create()
