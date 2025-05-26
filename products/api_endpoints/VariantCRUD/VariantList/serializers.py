from rest_framework import serializers

from products.models import ProductVariant

class VariantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = ['id' ,'name', 'product', 'size', 'color', 'price', 'stock', 'is_active', 'images']