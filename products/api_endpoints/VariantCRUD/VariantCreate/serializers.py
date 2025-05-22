from rest_framework import serializers
from products.models import Product, ProductVariant
from common.models import MediaFile

class ProductVariantCreateSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    images = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=MediaFile.objects.all(),
        required=False
    )

    class Meta:
        model = ProductVariant
        fields = ['name', 'product', 'size', 'color', 'price', 'stock', 'is_active', 'images']

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be a positive number.")
        return value

    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError("Stock cannot be negative.")
        return value

    def create(self, validated_data):
        images_data = validated_data.pop('images', [])
        variant = ProductVariant.objects.create(**validated_data)
        if images_data:
            variant.images.set(images_data)
        return variant