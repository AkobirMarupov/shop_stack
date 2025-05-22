from rest_framework.generics import DestroyAPIView
from rest_framework.response import Response

from products.api_endpoints.BrandCRUD.BrandDelete.serializers import BrandDeleteSerializer
from products.models import Brand


class BrandDeleteAPIView(DestroyAPIView):
    queryset = Brand.objects.all()  
    serializer_class = BrandDeleteSerializer
    permission_classes = []
    lookup_field = "pk"


    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            brand = Brand.objects.get(pk=pk)
        except Brand.DoesNotExist:
            return Response({"error": "Brand not found"}, status=404)
        
        brand.delete()
        return Response({"message": "Brand muvafaqqiyatli o'chirildi!"}, status=200) 