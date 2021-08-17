from typing import Any, Callable, List, Optional, Sequence

from env_config import settings
from fastapi import FastAPI
from routers.basic_router.basic_router import router
from routers.example_router.example_router import example_router


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

        return api
