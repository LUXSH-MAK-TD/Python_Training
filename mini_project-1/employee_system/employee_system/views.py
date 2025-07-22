from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MessageForm
from .models import Message
from django.contrib import messages as django_messages

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('dashboard')  # Redirect to dashboard after registration/login
    else:
        form = RegistrationForm()
    
    return render(request, 'registration/register.html', {'form': form})

def index_view(request):
    return render(request, 'registration/index.html')

@login_required
def dashboard_view(request):
    return render(request, 'registration/dashboard.html', {
        'user': request.user
    })

def send_message_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            django_messages.success(request, 'Message sent successfully!')
            return redirect('send_message')
    else:
        form = MessageForm()
    return render(request, 'registration/send_message.html', {'form': form})

@login_required
def inbox_view(request):
    messages = Message.objects.filter(recipient=request.user).order_by('-timestamp')  # type: ignore[attr-defined]
    return render(request, 'registration/inbox.html', {'messages': messages})