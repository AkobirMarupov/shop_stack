from rest_framework import serializers

from products.models import ProductVariant

class VariantDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = ['id']