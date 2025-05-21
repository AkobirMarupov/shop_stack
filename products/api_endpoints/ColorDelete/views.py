from rest_framework.generics import DestroyAPIView

from products.api_endpoints.ColorDelete.serializers import ColorDeleteSerializer
from products.models import Color


class ColorDeleteAPIView(DestroyAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorDeleteSerializer
    permission_classes = ['pk']

    