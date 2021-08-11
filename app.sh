#!/bin/bash

BINPATH=`dirname $0`
cd $BINPATH/..

HOST='0.0.0.0:8000'
WORKERS=1

APP='app'

if [ ! -z ${UVICORN_WORKERS} ]; then WORKERS=${UVICORN_WORKERS}; fi

if [ "$1" = "--reload" ]
then
    echo "--reload option enabled"
    uvicorn -w ${WORKERS} --env-file "./local.env" -b ${HOST} -t ${GUNICORN_WORKER_TIMEOUT} ${APP} --reload
else
    uvicorn -w ${WORKERS} --env-file "./local.env" -b ${HOST} -t ${GUNICORN_WORKER_TIMEOUT} ${APP}
fi
