from fastapi import Request, Response
from starlette.responses import StreamingResponse
from middleware.base import BaseMiddleware
import datetime
from utils.logger import Logger


class Timing(BaseMiddleware):
    @staticmethod
    async def process_request(request: Request) -> Request:
        request.state.start_time = datetime.datetime.now()
        Logger().info(
            msg=f'INCOMING REQUEST: {request.method.upper()} {request.url.path}',
            method=request.method.upper(),
            endpoint=request.url.path,
            ip_address=request.client.host
        )
        return request

    @staticmethod
    async def process_response(request: Request, response: StreamingResponse) -> Response:
        took = round(
            (datetime.datetime.now() - request.state.start_time).total_seconds() * 1000, 2)

        Logger().info(
            msg=f'OUTGOING RESPONSE: {request.method.upper()} {request.url.path} status_code: {response.status_code} took {took} ms',
            method=request.method.upper(),
            endpoint=request.url.path,
            ip_address=request.client.host,
            status=response.status_code,
            took=int(round(took, 0)),
        )
        return response
