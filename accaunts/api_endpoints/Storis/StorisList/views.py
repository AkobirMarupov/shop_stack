from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from accaunts.models import Story
from accaunts.api_endpoints.Storis.StorisList.serializers import StorySerializer


class StoryListAPIView(ListAPIView):
    serializer_class = StorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Story.objects.all().order_by('-expires_at')
    

class StoryDetailAPIView(RetrieveAPIView):
    serializer_class = StorySerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_object(self):
        try:
            return Story.objects.get(id=self.kwargs['id'])
        except Story.DoesNotExist:
            raise NotFound(detail="Story not found", code=404)
    
 