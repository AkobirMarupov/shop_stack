from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.parsers import MultiPartParser, FormParser

from products.models import ProductVariant
from products.api_endpoints.VariantCRUD.VariantCreate.serializers import ProductVariantCreateSerializer
from common.models import MediaFile


class ProductVariantCreateAPIView(CreateAPIView):
    serializer_class = ProductVariantCreateSerializer
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(
        operation_description="Create new product variant with image uploads",
        manual_parameters=[
            openapi.Parameter('name', openapi.IN_FORM, type=openapi.TYPE_STRING, required=True),
            openapi.Parameter('product', openapi.IN_FORM, type=openapi.TYPE_INTEGER, required=True),
            openapi.Parameter('size', openapi.IN_FORM, type=openapi.TYPE_INTEGER, required=False),
            openapi.Parameter('color', openapi.IN_FORM, type=openapi.TYPE_INTEGER, required=False),
            openapi.Parameter('price', openapi.IN_FORM, type=openapi.TYPE_INTEGER, required=True),
            openapi.Parameter('stock', openapi.IN_FORM, type=openapi.TYPE_INTEGER, required=True),
            openapi.Parameter('is_active', openapi.IN_FORM, type=openapi.TYPE_BOOLEAN, required=False),
            openapi.Parameter(
                'images',
                openapi.IN_FORM,
                type=openapi.TYPE_FILE,
                required=False,
                description='Multiple images (can upload multiple)'
            ),
        ],
        responses={201: ProductVariantCreateSerializer}
    )
    def post(self, request, *args, **kwargs):

        image_files = request.FILES.getlist('images')


        image_objs = []
        for image_file in image_files:
            media = MediaFile.objects.create(file=image_file)
            image_objs.append(media)


        mutable_data = request.data.copy()
        mutable_data.setlist('images', [str(media.id) for media in image_objs])

        serializer = self.get_serializer(data=mutable_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {
                'message': 'Product variant created with uploaded images',
                'data': serializer.data
            },
            status=status.HTTP_201_CREATED,
            headers=headers
        )
