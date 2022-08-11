from django.db import models

# Create your models here.

from users.models import CustomUser

class Track(models.Model):

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.CharField(blank=True, max_length=300)
    color = models.CharField(max_length=30, blank=True)

    def __str__(self):

        return self.title + ' - ' + self.user.email
