import sys

from env_config import settings
from fastapi import FastAPI
from fastapi_load import FastAPIStarter
from utils.db.database import create_db_and_tables
from utils.logger import Logger
from middlewares import custom_middlewares_list
from routers import routers_list

version = f"{sys.version_info.major}.{sys.version_info.minor}"

class App:
    async def on_startup(self):
        try:
            Logger(class_name=__name__).info(
                msg=f"{settings.project_name} STARTING...Using python version {version} and Uvicorn with Gunicorn"
            )
        except Exception as e:
            Logger(class_name=__name__).error(e)
            raise e

    async def on_shutdown(self):
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


if settings.db_url == "sqlite:///database.db":
    Logger().info(
        msg=f"Starting Database and Tables"
    )
    create_db_and_tables()

app = App().create()
