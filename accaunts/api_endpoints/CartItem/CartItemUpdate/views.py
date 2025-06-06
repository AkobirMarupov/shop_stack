from rest_framework.generics import GenericAPIView
from rest_framework import permissions

from accaunts.models import CartItem
from accaunts.api_endpoints.CartItem.CartItemUpdate.serializers import CartItemUpdateSerializer


class CartItemsUpdateAPIView(GenericAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

__all__ = ["CartItemsUpdateAPIView"]