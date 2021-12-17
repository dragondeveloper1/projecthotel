# User Serializer
from rest_framework import serializers
from rest_framework_simplejwt.tokens import Token
from .models import CustomUser,userAddresses
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
# from django.db import transaction
# from rest_auth.registration.serializers import RegisterSerializer
class RegisterSerializer(serializers.ModelSerializer):
    contactno = serializers.CharField(max_length=50)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50,min_length=8,write_only=True)
    # @transaction.atomic
    # def save(self, request):
    #     user = super().save(request)
    #     user.first_name = self.data.get('first_name')
    #     user.last_name = self.data.get('last_name')
    #     user.contactno = self.data.get('contactno')
    #     user.save()
    #     return user
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name','contactno','password']
    def validate(self,attrs):
        email = attrs.get('email','')
        return super().validate(attrs)
    def create(self,validated_data):
        return CustomUser.objects.create_user(**validated_data)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name','contactno','password']
class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = userAddresses
        fields = "__all__"
class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)
    tokens = serializers.CharField(max_length=68,min_length=6,read_only=True)
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'tokens']
    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        filtered_user_by_email = CustomUser.objects.filter(email=email)
        user = auth.authenticate(email=email, password=password)
        if filtered_user_by_email.exists() and filtered_user_by_email[0].auth_provider != 'email':
            raise AuthenticationFailed(
                detail='Please continue your login using ' + filtered_user_by_email[0].auth_provider)
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')
        if not user.is_verified:
            raise AuthenticationFailed('Email is not verified')
        return {
            'email': user.email,
            'username': user.username,
            'tokens': user.tokens
        }
        return super().validate(attrs)



