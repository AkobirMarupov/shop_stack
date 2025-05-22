from rest_framework.generics import CreateAPIView

from products.api_endpoints.ColorCRUD.ColorCreate.serializrers import ColorCreateSerializer
from products.models import Color

class ColorCreateAPIView(CreateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorCreateSerializer
    permission_classes = []