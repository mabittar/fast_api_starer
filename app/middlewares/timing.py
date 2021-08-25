from middlewares.base import BaseMiddleware
from utils.logger import Logger
import datetime
from fastapi import Request, Response


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
    async def process_response(request: Request, response: Response):

        process_time = round(
            (datetime.datetime.now() - request.state.start_time).total_seconds() * 1000, 3)
        response.headers["Process Time"] = str(process_time)
        Logger().info(
            msg=f'Process Time: {request.method.upper()} {request.url.path} status_code: {response.status_code} took {process_time} ms',
            method=request.method.upper(),
            endpoint=request.url.path,
            ip_address=request.client.host,
            status=response.status_code,
            took=int(round(process_time, 0)),
        )

        return response

