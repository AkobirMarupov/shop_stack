from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response

from products.api_endpoints.SizeCRUD.SizeUpdate.serializers import SizeUpdateSerializer
from products.models import Size


class SizeUpdateAPIView(UpdateAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeUpdateSerializer
    permission_classes = []
    lookup_field = "pk"
    
    def patch(self, request, pk):
        try:
            size = Size.objects.get(pk=pk)
        except Size.DoesNotExist:
            return Response({"error": "Size not found"}, status=404)
        
        serializers = SizeUpdateSerializer(size, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response({"message": "Size updated successfully"}, status=200)
        return Response(serializers.errors, status=400)

    