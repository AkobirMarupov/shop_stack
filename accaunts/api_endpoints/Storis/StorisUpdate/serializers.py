from rest_framework import serializers

from accaunts.models import Story


class StoryUpdateSerializer(serializers.ModelSerializer):
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
]
        read_only_fields = ['id']

    