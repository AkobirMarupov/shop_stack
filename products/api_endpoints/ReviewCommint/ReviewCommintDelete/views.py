from rest_framework.generics import DestroyAPIView
from rest_framework import permissions

from products.models import Review, Commint


class ReviewDeleteAPIView(DestroyAPIView):
    queryset = Review.objects.all()
    permission_classes = [permissions.IsAdminUser]
    lookup_field = 'id'


class CommintDeleteAPIView(DestroyAPIView):
    queryset = Commint.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'