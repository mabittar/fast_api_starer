#!/bin/bash

HOST='0.0.0.0'
PORT='8000'
WORKERS=1
TIMEOUT=50

APP='./app/main'

if [ ! -z ${UVICORN_WORKERS} ]; then WORKERS=${UVICORN_WORKERS}; fi

if [ "$1" = "--reload" ]
then
    echo "--reload option enabled"
    python -B ${APP}.py --reload
else
    gunicorn -k uvicorn.workers.UvicornWorker --threads 3 --timeout 0 --graceful-timeout ${TIMEOUT} --keep-alive ${TIMEOUT} --forwarded-allow-ips="*" --log-level 'warning' -w ${WORKERS} -b ${HOST}:${PORT} ${APP}
fi
