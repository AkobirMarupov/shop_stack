from rest_framework import serializers

from accaunts.models import Story


class StoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ['title', 'content', 'image', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

    