
from routers.basic_router import router
from routers.example_router import example_router
from fastapi import FastAPI, Request
from typing import Any, Callable, List, Optional, Sequence
from env_config import settings
from fastapi.middleware.cors import CORSMiddleware


class FastAPIStarter:
    @classmethod
    def create(
        cls,
        title: str = settings.project_name,
        middlewares: Optional[List] = None,
        on_startup: Optional[Sequence[Callable[[], Any]]] = None,
        on_shutdown: Optional[Sequence[Callable[[], Any]]] = None,
    ) -> FastAPI:

        swagger_url = f"/docs/"

        api = FastAPI(
            title=title,
            docs_url=swagger_url,
            on_startup=on_startup,
            on_shutdown=on_shutdown,
        )

        api.include_router(router)
        api.include_router(example_router)

        if middlewares:
            for middleware in middlewares[::-1]:
                api.add_middleware(middleware)
        
        api.add_middleware(
            CORSMiddleware,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],)

        return api


