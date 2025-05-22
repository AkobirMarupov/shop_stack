from rest_framework.generics import UpdateAPIView

from products.models import Category
from products.api_endpoints.CategoryCRUD.CategoryUpdate.serializers import CategoryUpdateSerializer



class CategoryUpdateAPIView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryUpdateSerializer
    permission_classes = []