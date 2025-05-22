from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from products.models import Size
from products.api_endpoints.SizeCRUD.SizeList.serializers import SizeSerializer

class SizeListAPIView(ListAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer
    permission_classes = []

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class SizeRetrieveAPIView(RetrieveAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer
    permission_classes = []
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
