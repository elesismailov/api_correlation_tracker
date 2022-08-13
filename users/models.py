
# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

from .helpers import generate_key

class CustomUser(AbstractUser):

    username    = models.CharField(max_length=30, unique=True)

    password    = models.CharField(max_length=100)
    email       = models.EmailField(max_length=100, unique=True)
    api_key     = models.CharField(max_length=100)

    created     = models.DateTimeField(editable=False)
    modified    = models.DateTimeField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''

        if not self.id:

            # TODO Generate random string

            self.api_key = generate_key()
            
            self.created = timezone.now()

        self.modified = timezone.now()

        return super(CustomUser, self).save(*args, **kwargs)

    def __str__(self):
        return self.email
