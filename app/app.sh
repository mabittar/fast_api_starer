#!/bin/bash
pwd

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


# #!/bin/bash sh

# set -e
# pwd

# if [ -f .main.py ]; then
#     DEFAULT_MODULE_NAME=main
# elif [ -f ./app/main.py ]; then
#     DEFAULT_MODULE_NAME=main
# fi
# MODULE_NAME=${MODULE_NAME:-$DEFAULT_MODULE_NAME}
# VARIABLE_NAME=${VARIABLE_NAME:-app}
# export APP_MODULE=${APP_MODULE:-"$MODULE_NAME:$VARIABLE_NAME"}

# if [ -f ./app/gunicorn_conf.py ]; then
#     DEFAULT_GUNICORN_CONF=./app/gunicorn_conf.py
# else
#     DEFAULT_GUNICORN_CONF=gunicorn_conf.py
# fi
# GUNICORN_CONF=${GUNICORN_CONF:-$DEFAULT_GUNICORN_CONF}
# export GUNICORN_CONF=${GUNICORN_CONF:-$DEFAULT_GUNICORN_CONF}

# if [ ! -z ${UVICORN_WORKERS} ]; then WORKERS=${UVICORN_WORKERS}; fi
# if [ ! -z ${WORKER_CLASS}]; then ${WORKER_CLASS:-"uvicorn.workers.UvicornWorker"}; fi


# if [ "$1" = "--reload" ]
# then
#     echo "--reload option enabled"
#     exec gunicorn -k "$WORKER_CLASS" -c "$GUNICORN_CONF" "$APP_MODULE"
# else
#     gunicorn -k uvicorn.workers.UvicornWorker --threads 3 --timeout 0 --graceful-timeout ${TIMEOUT} --keep-alive ${TIMEOUT} --forwarded-allow-ips="*" --log-level 'warning' -w ${WORKERS} -b ${HOST}:${PORT} ${APP}
# fi