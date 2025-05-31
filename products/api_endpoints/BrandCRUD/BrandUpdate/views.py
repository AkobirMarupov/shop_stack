from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework import parsers, status

from products.api_endpoints.BrandCRUD.BrandUpdate.serializers import BrandUpdateSerializer
from products.models import Brand

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class BrandUpdateAPIView(UpdateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandUpdateSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    lookup_field = "pk"

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('name', openapi.IN_FORM, type=openapi.TYPE_STRING, required=False),
            openapi.Parameter('slug', openapi.IN_FORM, type=openapi.TYPE_STRING, required=False),
            openapi.Parameter('logo', openapi.IN_FORM, type=openapi.TYPE_FILE, required=False),
        ]
    )
    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Updated successfully'}, status=status.HTTP_200_OK)
