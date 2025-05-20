from rest_framework import serializers

from products.models import Category


class CategoryDeleteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id']