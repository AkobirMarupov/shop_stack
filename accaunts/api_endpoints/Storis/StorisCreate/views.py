# accaunts/views.py
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from accaunts.models import Story
from accaunts.api_endpoints.Storis.StorisCreate.serializers import StoryCreateSerializer

class StoryCreateAPIView(CreateAPIView):
    serializer_class = StoryCreateSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(
        operation_summary="Create a new story",
        request_body=StoryCreateSerializer,
        responses={
            201: openapi.Response(description="Story created", schema=StoryCreateSerializer),
            400: "Bad Request"
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
