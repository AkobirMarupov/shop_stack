from rest_framework.serializers import ModelSerializer

from products.models import Review, Commint


class ReviewUpdateSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = ["id", "rating", "review", "product"]
        read_only_fields = ["id"]


class CommintUpdateSerializer(ModelSerializer):
    class Meta:
        model = Commint
        fields = [
            "id",
            "product",
            "user",
            "commint",
            "parent",
        ]
        read_only_fields = ["id"]