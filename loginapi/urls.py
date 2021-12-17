from allauth.account.views import confirm_email
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from .views import RegisterView,VerifyEmail,LoginAPIView,UserAPIView,UserAddressAPIView
# from users_api.views import MyObtainTokenPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/',RegisterView.as_view(),name="register"),
    path('email-verify',VerifyEmail.as_view(),name="email-verify"),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('user/',UserAPIView.as_view(),name="user"),
    path('userregister', UserAddressAPIView.as_view(), name="userregister"),
    # path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    # path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #url(r'^rest-auth/', include('dj_rest_auth.urls')),
    #url(r'^rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    url(r'^account/', include('allauth.urls')),
    url(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),
]