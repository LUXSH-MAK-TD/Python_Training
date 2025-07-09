from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta

@shared_task
def send_welcome_email(user_email):
    send_mail(
        'Welcome to Our Site',
        'Thank you for registering!',
        'from@example.com',
        [user_email],
        fail_silently=False,
    )

@shared_task
def cleanup_old_records():
    from myapp.models import SomeModel  # replace with your model
    threshold_date = timezone.now() - timedelta(days=30)
    deleted_count, _ = SomeModel.objects.filter(created_at__lt=threshold_date).delete()
    return f'Deleted {deleted_count} old records.'
