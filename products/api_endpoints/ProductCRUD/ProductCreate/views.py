from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status

from products.api_endpoints.ProductCRUD.ProductCreate.serializers import ProductCreateSerializer
from products.models import Product


class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer 

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
