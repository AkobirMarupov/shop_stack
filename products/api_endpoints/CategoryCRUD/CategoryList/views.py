from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView, ListAPIView

from products.models import Category
from products.api_endpoints.CategoryCRUD.CategoryList.serializers import CategoryListSerializer


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    permission_classes = []

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class CategoryRetrieveAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    permission_classes = []
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
