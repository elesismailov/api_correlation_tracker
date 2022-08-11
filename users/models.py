
# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):

    username = models.CharField(max_length=30, unique=True)

    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    api_key = models.CharField(max_length=100)


    def __str__(self):
        return self.email
