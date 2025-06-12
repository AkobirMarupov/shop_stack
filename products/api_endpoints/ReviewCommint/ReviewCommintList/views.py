from rest_framework.generics import ListAPIView
from rest_framework import permissions

from products.models import Review, Commint
from products.api_endpoints.ReviewCommint.ReviewCommintList.serializers import (
    UserReviewListSerializer,
    UserCommintSerializer
)


class UserReviewListAPIView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserReviewListSerializer

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user).order_by('-created_at') 
    
    

class UserCommintListAPIView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserCommintSerializer

    def get_queryset(self):
        return Commint.objects.filter(user=self.request.user).order_by('-created_at') 