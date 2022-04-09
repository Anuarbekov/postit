from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Post(models.Model):
    title = models.CharField(max_length=100, null=False)
    text = models.CharField(max_length=500, null=False, default='')
    date = models.DateTimeField(default=datetime.now, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.title, self.owner
