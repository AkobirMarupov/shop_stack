from rest_framework import serializers

from accaunts.models import Story


class StoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = [
            'id', 
            'user',
            'title',
            'description',
            'image',
            'video',
            'expires_at',
            'is_active',
]
        read_only_fields = ['id']

    