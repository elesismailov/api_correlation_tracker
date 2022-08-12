from django.db import models
from django.utils import timezone

# Create your models here.

from users.models import CustomUser

class Track(models.Model):

    user        = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title       = models.CharField(max_length=30)
    description = models.CharField(blank=True, max_length=300)
    color       = models.CharField(max_length=30, blank=True)

    created     = models.DateTimeField(editable=False)
    modified    = models.DateTimeField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''

        if not self.id:
            self.created = timezone.now()

        self.modified = timezone.now()

        return super(Track, self).save(*args, **kwargs)

    
    def __str__(self):

        return self.title + ' - ' + self.user.email
