from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

from accaunts.api_endpoints.Profile.RegisterReset.token import (
    generate_email_verification_token,
    verify_email_verification_token
)

User = get_user_model()


class RegisterResetSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    token = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'token']
        read_only_fields = ['id', 'token']

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            is_active=False  
        )
        user.set_password(validated_data['password'])
        user.save()
        
        user.token = generate_email_verification_token(user)
        return user


class RegisterVerifySerializer(serializers.Serializer):
    token = serializers.CharField()

    def validate_token(self, value):
        user_id = verify_email_verification_token(value)
        if not user_id:
            raise serializers.ValidationError("Invalid or expired token.")
        try:
            self.user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise serializers.ValidationError("User not found.")
        return value

    def save(self):
        self.user.is_active = True
        self.user.save()
        return self.user