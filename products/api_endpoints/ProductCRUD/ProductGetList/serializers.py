from rest_framework import serializers
from products.models import Product

class ProductListGSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'is_active']