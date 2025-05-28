from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import permissions

from accaunts.api_endpoints.CartItem.CartItemList.serializers import CartItemsSerializers
from accaunts.models import CartItem


class CartItemsListAPIView(GenericAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemsSerializers
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True )

        return Response(serializer.data)

