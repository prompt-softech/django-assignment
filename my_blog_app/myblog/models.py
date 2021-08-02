from django.db import models
from django.utils import timezone

# Create your models here.

class UserMessage(models.Model):
    message_id = models.AutoField
    username = models.CharField(max_length=25,null=True)
    text_message = models.CharField(max_length=1000)
    time_added = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.username

