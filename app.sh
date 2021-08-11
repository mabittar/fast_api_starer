#!/bin/bash

for arg; do
  case $1 in
  -l | --local)
    shift && LOCAL=1
    ;;
  -r | --reload)
    shift && RELOAD=1
    ;;
  esac
done

APP='main'
HOST='0.0.0.0'
PORT=8000
WORKERS=1

if [ ! -z ${UVICORN_WORKERS} ]; then WORKERS=${UVICORN_WORKERS}; fi

if [ "$LOCAL" = "1" ]; then
  echo "--local option enabled"
  BINPATH=$(dirname $0)
  cd $BINPATH/../../src

  if [ "$RELOAD" = "1" ]; then
    echo "--reload option enabled"
    python -B ${APP}.py
  else
    uvicorn -k uvicorn.workers.UvicornWorker --forwarded-allow-ips="*" --log-level 'warning' -w ${WORKERS} -b ${HOST}:${PORT} ${APP}
  fi
else
  echo "production ready"
  if [ "$RELOAD" = "1" ]; then
    echo "--reload option enabled"
    uvicorn -k uvicorn.workers.UvicornWorker --forwarded-allow-ips="*" --log-level 'warning' -w ${WORKERS} -b ${HOST}:${PORT} ${APP} --reload
  else
    uvicorn -k uvicorn.workers.UvicornWorker --forwarded-allow-ips="*" --log-level 'warning' -w ${WORKERS} -b ${HOST}:${PORT} ${APP}
  fi
fi
