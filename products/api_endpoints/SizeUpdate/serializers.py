from rest_framework import serializers

from products.models import Size

class SizeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['name', 'slug']
        extra_kwargs = {
            'name': {'required': False},
            'slug': {'required': False},
        }
