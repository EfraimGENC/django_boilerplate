import os
from celery import Celery
from celery.schedules import crontab


# Set the default Django settings module for the 'celery' program.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings.local')
if "DJANGO_SETTINGS_MODULE" not in os.environ:
    raise Exception(
        "DJANGO_SETTINGS_MODULE must be set in the environment before running celery."
    )

app = Celery('src')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


# SCHEDULED PERIODIC TASKS
###############################################################################
app.conf.timezone = 'Europe/Istanbul'
app.conf.beat_schedule = {
    'dummy_task': {
        'task': 'src.apps.core.tasks.dummy_task',
        'schedule': crontab(minute='*')
    },
}
