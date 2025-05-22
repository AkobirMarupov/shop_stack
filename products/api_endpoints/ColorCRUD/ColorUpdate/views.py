from rest_framework.generics import UpdateAPIView

from products.api_endpoints.ColorCRUD.ColorUpdate.serializers import ColorUpdateSerializer
from products.models import Color

class ColorUpdateAPIView(UpdateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorUpdateSerializer
    permission_classes = []