from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser, FormParser

from products.models import Review, Commint
from products.api_endpoints.ReviewCommint.ReviewCommentUpdate.serializers import ReviewUpdateSerializer, CommintUpdateSerializer

class ReviewUpdateAPIView(UpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewUpdateSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    lookup_field = 'id'

    @swagger_auto_schema(
        operation_summary="Update a review",
        operation_description="Update an existing review by its ID.",
        request_body=ReviewUpdateSerializer,
        responses={
            200: "Review updated successfully.",
            400: "Invalid data provided.",
            404: "Review not found.",
        },
    )
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    

class CommintUpdateAPIView(UpdateAPIView):
    queryset = Commint.objects.all()
    serializer_class = CommintUpdateSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    lookup_field = 'id'

    @swagger_auto_schema(
        operation_summary="Update a comment",
        operation_description="Update an existing comment by its ID.",
        request_body=CommintUpdateSerializer,
        responses={
            200: "Comment updated successfully.",
            400: "Invalid data provided.",
            404: "Comment not found.",
        },
    )
    def update(self, request, *args, **kwargs):
        isinstance = self.get_object()
        serializer = self.get_serializer(isinstance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
