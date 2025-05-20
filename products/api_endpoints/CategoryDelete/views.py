from rest_framework.generics import DestroyAPIView

from products.models import Category
from products.api_endpoints.CategoryDelete.serializers import CategoryDeleteSerializers


class CategoryDeleteAPIView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDeleteSerializers
    permission_classes = []
    lookup_field = 'pk'