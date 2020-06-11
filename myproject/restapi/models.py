from django.db import models
from django.contrib.auth.models import AbstractUser

class Blogger(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField(max_length=500)
