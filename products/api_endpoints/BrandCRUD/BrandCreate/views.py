from rest_framework.generics import CreateAPIView
from rest_framework import permissions, parsers

from products.api_endpoints.BrandCRUD.BrandCreate.serializers import BrandCreateSerializer
from products.models import Brand

class BrandCreateAPIView(CreateAPIView):
    queryset = Brand.objects.all()  
    serializer_class = BrandCreateSerializer
    permission_classes = [permissions.IsAdminUser]
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]

    