#!/bin/sh

case "$1" in
  "backend")
    uvicorn main:app --workers $UVICORN_WORKERS --host $UVICORN_HOST --port $UVICORN_PORT --root-path $API_PREFIX
    ;;
  "migration")
    alembic upgrade head
    ;;
  *)
    echo "Incorrect parameter to sh script!."
    exit 1
    ;;
esac
