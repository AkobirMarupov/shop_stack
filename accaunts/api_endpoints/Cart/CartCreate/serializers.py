from rest_framework import serializers

from accaunts.models import Cart


class CartCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id']
        read_only_fields = ['id']