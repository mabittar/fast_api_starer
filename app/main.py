from utils.database import DBConnector
from utils.logger import Logger
from fastapi_load import FastAPIStarter
from fastapi import FastAPI, Request
from starlette import responses
import sys

version = f"{sys.version_info.major}.{sys.version_info.minor}"


class App:
    # def __init__(self, scope):
    #     assert scope["type"] == "http"
    #     self.scope = scope

    async def on_startup(self):
        DBConnector.create_engine()
        Logger().info(msg=f"STARTING...Using python version {version}")


    async def on_shutdown(self):
        DBConnector.close()
        Logger.info(msg="shutting down...")


# Create your endpoints here


    def create(self) -> FastAPI:
        api = FastAPIStarter.create(
            title="FastAPI Fast Starter Project",
            on_startup=[self.on_startup],
            on_shutdown=[self.on_shutdown],
        )

        return api


app = App().create()
