from utils.database import SQLConnector
from utils.logger import Logger
from fastapi_load import FastAPIStarter
from fastapi import FastAPI, Request
from starlette import responses
import sys

version = f"{sys.version_info.major}.{sys.version_info.minor}"


    
async def on_startup():
    SQLConnector.create_engine()
    Logger().info(msg=f"STARTING...Using python version {version}")


async def on_shutdown():
    SQLConnector.close()
    Logger.info(msg="shutting down...")


def create() -> FastAPI:
    api = FastAPIStarter.create(
        title="FastAPI Fast Starter Project",
        on_startup=[on_startup],
        on_shutdown=[on_shutdown],
    )

    return api


app = application = create()


def __run(port: int):
    host = environ.get("HOST", "0.0.0.0")
    try:
        run(
            "main:app",
            host=host,
            port=port,
            reload=True,
            use_colors=True,
            proxy_headers=True,
            log_level="WARNING".lower(),
        )
    except Exception:
        __run(port + 1)


if __name__ == "__main__":
    from uvicorn import run
    from os import environ

    initial_port = int(environ.get("POST", "8000"))
    __run(initial_port)
