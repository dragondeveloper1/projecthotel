from django.shortcuts import render
from rest_framework import permissions
from .models import Roominfo,Roomdetail,Packages
from .serializers import RoominfoSerializer, RoomdetailSerializer, PackagesSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
class ActionBasedPermission(AllowAny):
    def has_permission(self, request, view):
        for klass,actions in getattr(view, 'action_permissions', [].items):
            if view.action in actions:
                return klass().has_permission(request,view)
            return False

class Roominfo_viewSet(viewsets.ModelViewSet):
    queryset = Roominfo.objects.all()
    serializer_class = RoominfoSerializer
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id','category']
    permissions_class = (ActionBasedPermission)
    action_permissions = {
        AllowAny : ['list','retrieve'],
        IsAdminUser : ['update','create','destroy','partial_update']
    }
class Roomdetail_viewSet(viewsets.ModelViewSet):
    queryset = Roomdetail.objects.all()
    serializer_class = RoomdetailSerializer
    lookup_field = 'title'
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['name','category','price','slug']
    permissions_class = (ActionBasedPermission)
    action_permissions = {
        AllowAny : ['list','retrieve'],
        IsAdminUser : ['update','create','destroy','partial_update']
    }

class Packages_viewSet(viewsets.ModelViewSet):
    queryset = Packages.objects.all()
    serializer_class = PackagesSerializer
    loookup_field = 'title'
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['title','status','slug']
    permissions_class = (ActionBasedPermission)
    action_permissions = {
         AllowAny : ['list','retrieve'],
        IsAdminUser : ['update','create','destroy','partial_update']
       
    }
