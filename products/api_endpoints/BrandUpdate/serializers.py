from rest_framework import serializers

from products.models import Brand


class BrandUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name', 'slug', 'logo']
        extra_kwargs = {
            'name': {'required': False},
            'slug': {'required': False},
            'logo': {'required': False},
        }
        