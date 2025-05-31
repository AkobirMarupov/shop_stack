from rest_framework import serializers

from products.models import Brand

class BrandCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name', 'slug', 'logo']

    
    def validate_logo(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Logotip hajmi 2 mgb dan kam bolishi kerak')
        
        if not value.content_type.startswith('image/'):
            raise serializers.ValidationError('Faqat rasm fayllariga ruxsat beriladi')
        return value