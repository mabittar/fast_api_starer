#!/bin/bash

BINPATH=$(dirname $0)
cd $BINPATH/..

HOST='0.0.0.0'
PORT='8000'
WORKERS=1
GUNICORN_WORKER_TIMEOUT=50
LOCAL_ENV='/local.env'

APP='/app/main'

if [ ! -z ${UVICORN_WORKERS} ]; then WORKERS=${UVICORN_WORKERS}; fi

if [ "$1" = "--reload" ]
then
    echo "--reload option enabled"
    gunicorn -k uvicorn.workers.UvicornWorker --forwarded-allow-ips="*" --timeout-keep-alive ${GUNICORN_WORKER_TIMEOUT} --log-level 'warning' -w ${WORKERS} -b ${HOST}:${PORT} ${APP}
else
    gunicorn -k uvicorn.workers.UvicornWorker --forwarded-allow-ips="*" --timeout-keep-alive ${GUNICORN_WORKER_TIMEOUT} --log-level 'warning' -w ${WORKERS} -b ${HOST}:${PORT} ${APP}
fi
