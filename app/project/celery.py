import logging
import os

from celery import Celery
from celery.app import shared_task

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

app = Celery("project")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

logger = logging.getLogger(__name__)


@shared_task(ignore_result=True)
def test_task():
    logger.debug("test")
    return None


app.conf.enable_utc = True
