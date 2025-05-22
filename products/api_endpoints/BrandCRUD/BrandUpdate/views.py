from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response

from products.api_endpoints.BrandCRUD.BrandUpdate.serializers import BrandUpdateSerializer
from products.models import Brand


class BrandUpdateAPIView(UpdateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandUpdateSerializer
    permission_classes = []
    lookup_field = "pk"

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        if not instance:
            return Response({"error": "Brand not found"}, status=404)
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Brand updated successfully"}, status=200)
        return Response(serializer.errors, status=400)