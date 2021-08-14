#! /usr/bin/env sh
set -e

cd app/

if [ -f main.py ]; then
    DEFAULT_MODULE_NAME=main
elif [ -f /app/main.py ]; then
    DEFAULT_MODULE_NAME=main
fi
MODULE_NAME=${MODULE_NAME:-$DEFAULT_MODULE_NAME}
VARIABLE_NAME=${VARIABLE_NAME:-app}
export APP_MODULE=${APP_MODULE:-"$MODULE_NAME:$VARIABLE_NAME"}

if [ -f ./app/gunicorn_conf.py ]; then
    DEFAULT_GUNICORN_CONF=./app/gunicorn_conf.py
else
    DEFAULT_GUNICORN_CONF=gunicorn_conf.py
fi
GUNICORN_CONF=${GUNICORN_CONF:-$DEFAULT_GUNICORN_CONF}
export GUNICORN_CONF=${GUNICORN_CONF:-$DEFAULT_GUNICORN_CONF}

if [ ! -z ${UVICORN_WORKERS} ]; then WORKERS=${UVICORN_WORKERS}; fi

export WORKER_CLASS=${WORKER_CLASS:-"uvicorn.workers.UvicornWorker"}
pwd

exec gunicorn -k "$WORKER_CLASS" -c "$GUNICORN_CONF" "$APP_MODULE"
