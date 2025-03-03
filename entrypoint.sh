#!/bin/sh
if [ "$SERVICE" = "worker" ]; then
  watchmedo auto-restart --directory=./src --pattern="*.py" --recursive -- celery -A src.tasks worker --loglevel=info
elif [ "$SERVICE" = "web" ]; then
  watchmedo auto-restart --directory=./src --pattern="*.py" --recursive -- uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
else
  echo "No SERVICE specified. Exiting."
  exit 1
fi
