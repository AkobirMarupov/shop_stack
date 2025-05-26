from rest_framework.generics import DestroyAPIView

from products.api_endpoints.VariantCRUD.VariantDelete.serializers import VariantDeleteSerializer
from products.models import ProductVariant

class ProductVariantDeleteAPIView(DestroyAPIView):
    queryset = ProductVariant.objects.all()
    serializer_class = VariantDeleteSerializer
    permission_classes = []
    lookup_field = 'pk'