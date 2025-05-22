from rest_framework.generics import DestroyAPIView
from rest_framework.response import Response

from products.api_endpoints.SizeCRUD.SizeDelete.serializers import SizeDeleteSerializer
from products.models import Size

class SizeDeleteAPIView(DestroyAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeDeleteSerializer
    permission_classes = []

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            size = Size.objects.get(pk=pk)
        except Size.DoesNotExist:
            return Response({"error": "Size not found"}, status=404)
        
        size.delete()
        return Response({"message": "Mahsulot muvaffaqiyatli ochirildi"}, status=204)
