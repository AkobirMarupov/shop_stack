from rest_framework.views import APIView
from rest_framework.response import Response

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from accaunts.api_endpoints.Profile.PsswordReset.serializers import (
    PasswordResetRequestSerializer,
    PasswordResetConfirmSerializer
)

from accaunts.api_endpoints.Profile.PsswordReset.email_send import send_password_reset_email


class PasswordResetAPIView(APIView):
    @swagger_auto_schema(
            request_body=PasswordResetRequestSerializer
    )

    def post(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data, context={
            'send_email': send_password_reset_email
        })
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'detail': 'Parolni tiklash uchun elektron pochta xabari yuborildi.'}, status=200)
    

class PasswordResetConfirmAPIView(APIView):
    permission_classes = []
    @swagger_auto_schema(
        request_body=PasswordResetConfirmSerializer
    )
    def post(self, request):
        serializer = PasswordResetConfirmSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'detail': 'Parol muvaffaqiyatli tiklandi.'}, status=200)