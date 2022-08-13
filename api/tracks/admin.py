from django.contrib import admin

# Register your models here.
from .models import Track, TrackEntry

admin.site.register(Track)
admin.site.register(TrackEntry)
