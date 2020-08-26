from django.db import models
from user_app.models import ApiUser

# Create your models here.
class ChatRoom(models.Model):
    owner = models.ForeignKey(ApiUser, on_delete=models.CASCADE)
    target = models.ForeignKey(ApiUser, on_delete=models.CASCADE, related_name='targetuser')

    class Meta:
        unique_together = ('owner', 'target')
