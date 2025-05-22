from rest_framework.generics import ListAPIView

from products.api_endpoints.ProductCRUD.ProductGetList.serializers import ProductListGSerializer
from products.models import Product

class ProductListGetAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListGSerializer
    permission_classes = []
   
    

class ProductRetrieveAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListGSerializer
    permission_classes = []
    lookup_field = "pk"

    