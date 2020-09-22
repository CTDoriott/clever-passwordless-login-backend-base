from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from uuid import uuid4

class Autologin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    unique_value = models.CharField(max_length=45)
    created_at = models.DateTimeField(default=timezone.now)
    link_type = models.IntegerField()
