from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_daily_emails():
    User = get_user_model()
    emails = User.objects.values_list('email', flat=True)
    subject = "Daily Reminder"
    message = "Hello! Here’s your daily update."
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        list(emails),
        fail_silently=False,
    ) 