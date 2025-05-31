from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import parsers

from products.api_endpoints.BrandCRUD.BrandList.serializers import BrandSerializer
from products.models import Brand

class BrandListAPIView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = []
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]


    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)
    


class BrandRetrieveAPIView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = []
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    lookup_field = "pk"


    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    