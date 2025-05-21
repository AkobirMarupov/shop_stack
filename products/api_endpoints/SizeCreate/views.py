from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from products.api_endpoints.SizeCreate.serializers import SizeCreateSerializer
from products.models import Size

class SizeCreateAPIView(CreateAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeCreateSerializer
    permission_classes = []
