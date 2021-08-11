#!/bin/bash

BINPATH=`dirname $0`
cd $BINPATH/..

HOST='0.0.0.0'
PORT='8000'
WORKERS=1
GUNICORN_WORKER_TIMEOUT=50
LOCAL_ENV='../local.env'

APP='app:app'

if [ ! -z ${UVICORN_WORKERS} ]; then WORKERS=${UVICORN_WORKERS}; fi

if [ "$1" = "--reload" ]
then
    echo "--reload option enabled"
    uvicorn ${APP} --workers ${WORKERS} --env-file ${LOCAL_ENV} --host ${HOST} --port ${PORT} --timeout-keep-alive ${GUNICORN_WORKER_TIMEOUT} --reload
else
    uvicorn ${APP} --workers ${WORKERS} --env-file ${LOCAL_ENV} --host ${HOST} --port ${PORT} --timeout-keep-alive ${GUNICORN_WORKER_TIMEOUT}
fi
