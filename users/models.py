
# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.db import models

from .helpers import generate_key

class CustomUser(AbstractUser):

    username    = models.CharField(max_length=30, unique=True)

    password    = models.CharField(max_length=100)
    email       = models.EmailField(max_length=100, unique=True)
    api_key     = models.CharField(max_length=100, unique=True)

    created     = models.DateTimeField(editable=False)
    modified    = models.DateTimeField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''

        if not self.id:

            # TODO Generate random string

            api_key = generate_key()

            # if key somehow exists re-generate it
            while len(CustomUser.objects.filter(api_key=api_key)) != 0:
                api_key = generate_key()
                
            self.api_key = api_key
            
            self.created = timezone.now()

        self.modified = timezone.now()

        return super(CustomUser, self).save(*args, **kwargs)

    def __str__(self):
        return self.email
