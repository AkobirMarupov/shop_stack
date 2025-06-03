from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializers import RegisterResetSerializer, RegisterVerifySerializer
from accaunts.api_endpoints.Profile.RegisterReset.email_sends import send_verification_email



class RegisterResetAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(
        request_body=RegisterResetSerializer,
        responses={201: openapi.Response("Foydalanuvchi muvaffaqiyatli ro'yxatdan o'tdi.")}
    )
    def post(self, request):
        serializer = RegisterResetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        token = user.token
        send_verification_email(user, token)

        return Response({
            "detail": "Foydalanuvchi muvaffaqiyatli ro'yxatdan o'tdi. Hisobingizni tasdiqlash uchun elektron pochtangizni tekshiring."
        }, status=201)


class UserRegisterVerifyAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(
        request_body=RegisterVerifySerializer,
        responses={200: openapi.Response("Foydalanuvchi elektron pochtasi muvaffaqiyatli tasdiqlandi.")}
    )
    def post(self, request):
        serializer = RegisterVerifySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
            "detail": "Foydalanuvchi elektron pochtasi muvaffaqiyatli tasdiqlandi."
        }, status=200)
