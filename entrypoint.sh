#!/bin/sh
if [ "$SERVICE" = "worker" ]; then
  celery -A src.celery_app worker --loglevel=info
elif [ "$SERVICE" = "web" ]; then
  watchmedo auto-restart --recursive --pattern="*.py" -- python -m src.main  
else
  echo "No SERVICE specified. Exiting."
  exit 1
fi
