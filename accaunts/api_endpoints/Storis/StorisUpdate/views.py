from rest_framework.generics import UpdateAPIView
from rest_framework import permissions
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser, FormParser

from accaunts.models import Story
from accaunts.api_endpoints.Storis.StorisUpdate.serializers import StoryUpdateSerializer

class StoryUpdateAPIView(UpdateAPIView):
    queryset = Story.objects.all()
    serializer_class = StoryUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    lookup_field = 'id'

    @swagger_auto_schema(
        operation_summary="Update a story",
        operation_description="Update an existing story by its ID.",
        request_body=StoryUpdateSerializer,
        responses={
            200: "Story updated successfully.",
            400: "Invalid data provided.",
            404: "Story not found.",
        },
    )
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
