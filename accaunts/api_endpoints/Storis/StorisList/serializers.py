from rest_framework import serializers

from accaunts.models import Story


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ('id', 'user', 'title', 'description',
                   'image', 'video', 'expires_at')