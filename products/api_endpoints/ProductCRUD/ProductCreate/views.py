from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.parsers import MultiPartParser, FormParser

from products.api_endpoints.ProductCRUD.ProductCreate.serializers import ProductCreateSerializer
from products.models import Product
from common.models import MediaFile


class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(
        operation_description="Create new product with images",
        manual_parameters=[
            openapi.Parameter('name', openapi.IN_FORM, type=openapi.TYPE_STRING, required=True),
            openapi.Parameter('description', openapi.IN_FORM, type=openapi.TYPE_STRING, required=True),
            openapi.Parameter('brand', openapi.IN_FORM, type=openapi.TYPE_INTEGER, required=False),
            openapi.Parameter('slug', openapi.IN_FORM, type=openapi.TYPE_STRING, required=True),
            openapi.Parameter('is_active', openapi.IN_FORM, type=openapi.TYPE_BOOLEAN, required=False),
            openapi.Parameter('category', openapi.IN_FORM, type=openapi.TYPE_INTEGER, required=False),
            openapi.Parameter(
                name='default_images',
                in_=openapi.IN_FORM,
                type=openapi.TYPE_FILE,
                required=False,
                description='Multiple images (MediaFile)',
            ),
        ],
        responses={201: ProductCreateSerializer}
    )
    def post(self, request, *args, **kwargs):
        image_files = request.FILES.getlist('default_images')

        media_objs = []
        for img in image_files:
            media = MediaFile.objects.create(file=img)
            media_objs.append(media)


        mutable_data = request.data.copy()
        mutable_data.setlist('default_images', [str(media.id) for media in media_objs])

        serializer = self.get_serializer(data=mutable_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
