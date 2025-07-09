from django.shortcuts import render
from users.tasks import send_welcome_email

def user_registered(user):
    send_welcome_email.delay(user.email)


