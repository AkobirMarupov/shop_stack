from rest_framework.generics import UpdateAPIView

from products.api_endpoints.ProductCRUD.ProductUpdate.serializers import ProductUpdateSerializer
from products.models import Product

class ProductUpdateAPIView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductUpdateSerializer
    permission_classes = []
    lookup_field = 'pk'
    