from django import forms
from django.contrib.auth.models import User
from .models import Message

class MessageForm(forms.ModelForm):
    recipient = forms.ModelChoiceField(queryset=User.objects.all(), label="Send To")
    subject = forms.CharField(max_length=255)
    body = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Message
        fields = ['recipient', 'subject', 'body'] 