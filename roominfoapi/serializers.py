from rest_framework import serializers
from .models import Roominfo, Roomdetail,Packages

class RoominfoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Roominfo
        fields = "__all__"
class RoomdetailSerializer(serializers.ModelSerializer):
    class Meta:
        model= Roomdetail
        fields = "__all__"

class PackagesSerializer(serializers.ModelSerializer):
    class Meta:
        model= Packages
        fields = "__all__"
