from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from products.api_endpoints.VariantCRUD.VariantList.serializers import VariantListSerializer
from products.models import ProductVariant


class ProductVarianrListAPIView(ListAPIView):
    queryset = ProductVariant.objects.all()
    serializer_class = VariantListSerializer
    permission_classes = []
   
    

class ProductVariantRetrieveAPIView(ListAPIView):
    queryset = ProductVariant.objects.all()
    serializer_class = VariantListSerializer
    permission_classes = []
    lookup_field = "pk"
    