from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from products.api_endpoints.VariantCRUD.VariantUpdate.serializers import ProductVariantUpdateSerializer
from products.models import ProductVariant  


class ProductVariantUpdateAPIView(UpdateAPIView):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantUpdateSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def update(self, request, *args, **kwargs):
        queryset = super().get_queryset()
        product_id = self.request.query_params.get('product_id', None)
        if product_id:
            queryset = queryset.filter(product_id=product_id)
            
        return queryset