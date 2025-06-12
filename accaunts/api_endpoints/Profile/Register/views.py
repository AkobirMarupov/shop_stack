from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model

from accaunts.tokens import generate_email_confirm_token, generate_temporary_password, verify_email_confirm_token
from accaunts.email_send import send_email
from accaunts.models import Cart
from accaunts.api_endpoints.Profile.Register.serializers import ConfirmTokenSerializer, RegisterInputSerializer


User = get_user_model()

class RegisterUserAPIView(APIView):
    permission_classes = []

    @swagger_auto_schema(request_body=RegisterInputSerializer)
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response(
                {'detail': 'Email and password are required.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        existing = User.objects.filter(email=email, is_active=True).first()
        if existing:
            if not existing.is_confirmed:
                token = generate_email_confirm_token(user)
                new_pass = generate_temporary_password()
                existing.set_password(new_pass)
                existing.save()
                
                send_email(
                    subject="Tasdiqlash havolasi orqali prolinigizga start bering",
                    intro_text='Tasdiqlash uchun quyidagi havolani bosing.',
                email=email,
                token=token,
                template='email/reset_password_email.html',
                password=None
                )

                return Response (
                    {"detail": "Foydalanuvchi allaqachon mavjud, lekin hali tasdiqlanmagan. Tasdiqlash xati yuborildi."}, 
                    status=status.HTTP_200_OK
                )
            
            
            return Response(
                {"detail": "Ushbu e-pochta manzili allaqachon ro'yxatdan o'tkazilgan."}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        user = User.objects._create_user(email=email, password=password, is_confirmed=False)
        Cart.objects.create(user=user)
        token = generate_email_confirm_token(user)

        send_email(
            subject="Parolingizni qayta o'rnating", 
            intro_text="Tasdiqlash uchun quyidagi havolani bosing.", 
            email=email, 
            token=token, 
            template="email/reset_password_email.html",
        )

        return Response(
            {"detail": "Foydalanuvchi yaratildi. Tasdiqlash xati yuborildi."}, 
            status=status.HTTP_201_CREATED
        )
    
class RegisterConfirmAPIView(APIView):
    permission_classes = []

    @swagger_auto_schema(request_body=ConfirmTokenSerializer)
    def post(self, request):
        token = request.data.get('token')

        if not token:
            return Response({'detail': 'Token talab qilinadi.'}, status= status.HTTP_400_BAD_REQUEST)
        
        user_id = verify_email_confirm_token(token)
        
        if not user_id:
            return Response({'detail': 'Token yaroqsiz yoki muddati o`tgan.'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = User.objects.get(id=user_id)

        except User.DoesNotExist:
            return Response({"detail": "Foydalanuvchi topilmadi."}, status=status.HTTP_404_NOT_FOUND) 
        
        if user.is_confirmed:
            return Response({"detail": "Elektron pochta allaqachon tasdiqlangan."}, status=status.HTTP_400_BAD_REQUEST)

        user.is_confirmed = True
        user.save()

        return Response({"detail": "Elektron pochta muvaffaqiyatli tasdiqlandi."}, status=status.HTTP_200_OK)