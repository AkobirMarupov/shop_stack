from rest_framework.serializers import ModelSerializer

from products.models import Review, Commint


class ReviewCreateSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = ["id", "rating", "review", "product"]
        read_only_fields = ["id"]

        
