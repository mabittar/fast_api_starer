from typing import Callable

from fastapi import Request, Response
from starlette.applications import Starlette
from starlette.middleware.base import BaseHTTPMiddleware


class BaseMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: Starlette):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        request = await self.process_request(request=request)
        response = await call_next(request)
        response = await self.process_response(request=request, response=response)
        return response

    @staticmethod
    async def process_request(request: Request) -> Request:
        return request

    @staticmethod
    async def process_response(request: Request, response: Response) -> Response:
        return response
