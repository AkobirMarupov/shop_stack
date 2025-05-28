from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status

from accaunts.api_endpoints.Cart.CartList.serializers import CartSerializer
from accaunts.models import Cart


class CartListAPIView(ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = []

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    

class CartRetrieveAPIView(RetrieveAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    lookup_field = "pk"

    def get_object(self):
        try:
            return super().get_object()
        except:
            raise NotFound(detail="Bu ID boyicha cart topilmadi", code=404)