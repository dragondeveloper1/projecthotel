from rest_framework import serializers
from .models import Roombooking, Eventbooking
class RoombookingSerializer(serializers.ModelSerializer):
    class Meta:
        model= Roombooking
        fields = "__all__"

class EventbookingSerializer(serializers.ModelSerializer):
    class Meta:
        model= Eventbooking
        fields = "__all__"
