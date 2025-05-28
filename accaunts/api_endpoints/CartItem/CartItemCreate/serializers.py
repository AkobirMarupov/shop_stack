from rest_framework import serializers

from accaunts.models import CartItem


class CartItemCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['product', 'quantity']
