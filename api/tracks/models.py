from django.db import models

# Create your models here.

class User(models.Model):
    pass

class Track(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    track_id = models.IntegerField(primary_key=True, unique=True)
    title = models.CharField(max_length=30)
    description = models.CharField(blank=True, max_length=300)
    color = models.CharField(max_length=30)
