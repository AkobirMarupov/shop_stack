from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views import ApiView
from rest_framework import status

class SeeionLoginAPIView(ApiView):
    permisson_classes = []

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'})
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
        
        