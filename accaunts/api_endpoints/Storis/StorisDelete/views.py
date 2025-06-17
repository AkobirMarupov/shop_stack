from rest_framework.generics import DestroyAPIView
from rest_framework import permissions
from rest_framework.response import Response

from accaunts.models import Story


class StoryDeleteAPIView(DestroyAPIView):
    queryset = Story.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def perform_destroy(self, instance):
        print(f"Deleting story with ID: {instance.id}")
        super().perform_destroy(instance)
        return Response({"detail": "Story deleted successfully."}, status=204)