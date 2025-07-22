from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)  # type: ignore[assignment]

    def __str__(self):
        sender_username = self.sender.username  # type: ignore[attr-defined]
        recipient_username = self.recipient.username  # type: ignore[attr-defined]
        return f"From {sender_username} to {recipient_username}: {self.subject}" 