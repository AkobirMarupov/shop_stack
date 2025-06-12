from rest_framework.generics import CreateAPIView
from rest_framework import permissions

from products.models import Review, Commint
from products.api_endpoints.ReviewCommint.ReviewCommintCreatr.serializers import ReviewCreateSerializer

class ReviewCreateAPIView(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewCreateSerializer
    permission_classes = [permissions.IsAuthenticated]  

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
