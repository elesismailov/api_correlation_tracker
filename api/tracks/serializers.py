
from rest_framework import serializers
from .models import Track

class TrackSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Track
        fields = ['id', 'title', 'description', 'color', 'created', 'modified']
