from django.shortcuts import render
from rest_framework import generics,status
from .serializers import RegisterSerializer,LoginSerializer,UserSerializer,UserAddressSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser,userAddresses
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
from django.conf import settings

class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer 
    
    def post(self,request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = CustomUser.objects.get(email= user_data['email'])
        token = RefreshToken.for_user(user).access_token
        current_site = get_current_site(request).domain
        relativeLink = reverse('email-verify')
        print(relativeLink)
        absurl = 'http://'+ "192.168.2.102:8888" + str(relativeLink) +"?token="+str(token)
        email_body = 'Hi '+user.first_name +' Use the link below to verify your email' + absurl
        data = {'email_body': email_body, 'to_email': user.email,
                'email_subject': 'Verify your email'}
        print("i am sending mail")
        Util.send_mail(data)
        return Response(user_data,status = status.HTTP_201_CREATED)

class VerifyEmail(generics.GenericAPIView):
    def get(self,request):
        token = request.GET.get('token')
        try:
            print("i am verifying mail")
            payload = jwt.decode(token,settings.SECRET_KEY)
            user = CustomUser.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return Response({'email':'Successfully activated'},status = status.HTTP_200_OK)

        except jwt.ExpiredSignatureError as identifier:
            return Response({'error':'Activation Expired'},status = status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error':'Invalid Token'},status = status.HTTP_400_BAD_REQUEST)

class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        print(serializer)
        serializer.is_valid(raise_exception=True)
        print(serializer.is_valid)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
class UserAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    models = CustomUser
    queryset = CustomUser.objects.all()

class UserAddressAPIView(generics.ListAPIView):
    serializer_class = UserAddressSerializer
    models = userAddresses
    queryset = userAddresses.objects.all()