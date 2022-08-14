
from rest_framework import serializers
from .models import Track, TrackEntry

class TrackSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Track
        fields = ['id', 'title', 'description', 'color', 'created', 'modified']


class TrackEntrySerializer(serializers.ModelSerializer):

    class Meta:

        model = TrackEntry
        fields = ['id', 'date', 'rating']
