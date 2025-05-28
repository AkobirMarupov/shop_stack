from rest_framework import serializers

from products.models import ProductVariant


class CartItemsVariantSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = ['id', 'name', 'price']


class CartItemsSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    product = CartItemsVariantSerializers()
    quantity = serializers.IntegerField()
    
