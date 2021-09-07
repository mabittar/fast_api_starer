import sys

from env_config import settings
from fastapi import FastAPI
from fastapi_load import FastAPIStarter
from utils.db.database import SQLConnector, Base
from utils.logger import Logger
from middlewares import custom_middlewares_list
from routers import routers_list

version = f"{sys.version_info.major}.{sys.version_info.minor}"
# Create all models in local db
Base.metadata.create_all(bind=SQLConnector.get_engine())

class App:
    async def on_startup(self):
        try:
            Logger(class_name=__name__).info(
                msg=f"{settings.PROJECT_NAME} STARTING...Using python version {version} and Uvicorn with Gunicorn"
            )
            session = await SQLConnector.create_session()
            try:
                yield session

            except Exception as exc:
                session.rollback()
                raise exc
        except Exception as e:
            Logger(class_name=__name__).error(e)
            raise e

    async def on_shutdown(self):
        SQLConnector.close()
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

app = App().create()
