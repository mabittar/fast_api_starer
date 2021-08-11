
from framework.resources import router
from fastapi import FastAPI, Request
from typing import Any, Callable, List, Optional, Sequence
from starlette.responses import JSONResponse


class FastAPI:
    @classmethod
    def create(
        cls,

        title: str = None,
        middlewares: Optional[List] = None,
        on_startup: Optional[Sequence[Callable[[], Any]]] = None,
        on_shutdown: Optional[Sequence[Callable[[], Any]]] = None,
    ) -> FastAPI:

        swagger_url = f"/docs/"
        openapi_url = f"/docs/openapi_url.json"

        api = FastAPI(
            title=title,
            docs_url=swagger_url,
            openapi_url=openapi_url,
            on_startup=on_startup,
            on_shutdown=on_shutdown,
        )

        api.include_router(router)

        if middlewares:
            for middleware in middlewares[::-1]:
                api.add_middleware(middleware)

        return api


