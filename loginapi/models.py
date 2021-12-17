from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken
from .managers import CustomUserManager
# Create your models here.
AUTH_PROVIDERS = {'facebook': 'facebook', 'google': 'google',
                  'twitter': 'twitter', 'email': 'email'}
#webuser information, later information to be added here
class CustomUser(AbstractUser):
    username = None
    
    email = models.EmailField(_('email address'), unique=True)
    contactno = models.CharField(max_length=50,default="9841989898",null=False)
    is_verified = models.BooleanField(default=False)
    auth_provider = models.CharField(
        max_length=255, blank=False,
        null=False, default=AUTH_PROVIDERS.get('email'))
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    def __str__(self):
        return self.email
    def tokens(self):
        print("inside token")
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

#user address information
class userAddresses(models.Model):
    user_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='user_address')
    addressLine1 = models.CharField(max_length=250,default="your street/tole name", null=False)
    addressLine2 = models.CharField(max_length=250,blank=True,null=True)
    district = models.CharField(max_length=100,blank=True,null=True)
    province = models.CharField(max_length=100,blank=True,null=True)
    country = models.CharField(max_length=100,default= "Nepal",null=False)
    phone_number = models.CharField(max_length=100,default="phonenumbers",null=False)
  