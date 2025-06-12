from rest_framework import serializers

from products.models import Review, Commint, Product


class ReviewCommentProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name"] 


class UserReviewListSerializer(serializers.ModelSerializer):
    product = ReviewCommentProductSerializer()
    
    class Meta:
        model = Review
        fields = ["id", "product", "rating", "review", "created_at"]


class UserCommintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commint
        fields = ["id", "product", "commint", "parent", "created_at"]

    
    