from rest_framework.generics import ListAPIView

from products.api_endpoints.ColorCRUD.ColorList.serializers import ColorListSerializer
from products.models import Color


class ColorListAPIView(ListAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorListSerializer
    permission_classes = []


    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)
    

class ColorRetrieveAPIView(ListAPIView):
    queryset = Color.objects.all()      
    serializer_class = ColorListSerializer
    permission_classes = []
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)