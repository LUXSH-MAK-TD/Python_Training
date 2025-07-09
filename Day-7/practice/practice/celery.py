
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'practice.settings')

app = Celery('practice')

# Read config from Django settings, CELERY_ namespace
app.config_from_object('django.conf:settings', namespace='CELERY')

# Autodiscover tasks in installed apps
app.autodiscover_tasks()
