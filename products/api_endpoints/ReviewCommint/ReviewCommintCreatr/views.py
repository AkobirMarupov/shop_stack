from rest_framework.generics import CreateAPIView
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser
from drf_yasg.utils import swagger_auto_schema

from products.models import Review, Commint
from products.api_endpoints.ReviewCommint.ReviewCommintCreatr.serializers import (
    ReviewCreateSerializer, CommintCreateSerializer
)

class ReviewCreateAPIView(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewCreateSerializer
    permission_classes = [permissions.IsAuthenticated]  

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommintCreateAPIView(CreateAPIView):
    queryset = Commint.objects.all()
    serializer_class = CommintCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(
        operation_summary="Create a comment",
        operation_description="Create a new comment for a product.",
        request_body=CommintCreateSerializer,
        responses={
            201: "Comment created successfully.",
            400: "Invalid data provided.",
        },
    )
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)