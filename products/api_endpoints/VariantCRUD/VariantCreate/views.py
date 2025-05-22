from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from products.api_endpoints.VariantCRUD.VariantCreate.serializers import ProductVariantCreateSerializer


class ProductVariantCreateAPIView(CreateAPIView):
    serializer_class = ProductVariantCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {
                'message': 'Product variant created successfully',
                'data': serializer.data
            },
            status=status.HTTP_201_CREATED,
            headers=headers
        )