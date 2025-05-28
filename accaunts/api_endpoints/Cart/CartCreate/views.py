from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from accaunts.api_endpoints.Cart.CartCreate.serializers import CartCreateSerializers
from accaunts.models import Cart

class CartCreateAPIView(CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartCreateSerializers
    permission_classes = [IsAuthenticated]

    def post(self, serializer, *args, **kwargs):
        serializer.save(user=self.request.user)
