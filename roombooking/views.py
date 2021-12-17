from django.shortcuts import render
from rest_framework import permissions
from .models import Roombooking, Eventbooking
from .serializers import RoombookingSerializer,EventbookingSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response


# Create your views here.
class ActionBasedPermission(AllowAny):
    def has_permission(self, request, view):
        for klass,actions in getattr(view, 'action_permissions', [].items):
            if view.action in actions:
                return klass().has_permission(request,view)
            return False

class Roombooking_viewSet(viewsets.ModelViewSet):
    queryset = Roombooking.objects.all()
    serializer_class = RoombookingSerializer
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['category','name','check_in','check_out']
    permissions_class = (ActionBasedPermission)
    action_permissions = {
         AllowAny : ['list','retrieve'],
        IsAdminUser : ['update','create','destroy','partial_update']
       
    }

class Eventbooking_viewSet(viewsets.ModelViewSet):
    queryset = Eventbooking.objects.all()
    serializer_class = EventbookingSerializer
    lookup_field = 'title'
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['title']
    permissions_class = (ActionBasedPermission)
    action_permissions = {
         AllowAny : ['list','retrieve'],
        IsAdminUser : ['update','create','destroy','partial_update']
       
    }
    

class AvailableRoom(mixins.CreateModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    """
    API endpoint for adding and processing new client (by uid) face
    """
    queryset = Roombooking.objects.all()
    serializer_class = RoombookingSerializer
    permissions_class = (ActionBasedPermission)
    action_permissions = {
         AllowAny : ['list','retrieve'],
        IsAdminUser : ['update','create','destroy','partial_update']
       
    }

    def create(self, request):
        if request.POST:
            try:
                print("helo")
                print(request.data['check_in'])
                print(request.data['check_out'])
                print(request.data['category'])
                checkin= request.data['check_in']
                checkout = request.data['check_out']
                category = request.data['category']

                instance = Roombooking.filter_booking(self,checkin, checkout,category)
                print(instance)
                serializer = RoombookingSerializer(
                    instance=instance,
                    data=request.data
                )
            except Roombooking.DoesNotExist:
                serializer = RoombookingSerializer(data=request.data)
        else:
            serializer = RoombookingSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        # serializer.save()

        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = RoombookingSerializer(instance=instance)
        return Response(serializer.data)