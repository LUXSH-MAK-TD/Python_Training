import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'employee_system.settings')
app = Celery('employee_system')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'daily-emails': {
        'task': 'employee_system.tasks.send_daily_emails',
        'schedule': crontab(hour=18, minute=35),
    },
}
