from celery import Celery

# Create a Celery instance with the broker URL (matches docker-compose environment)
app = Celery('tasks', broker='redis://redis:6379/0')

import src.tasks

