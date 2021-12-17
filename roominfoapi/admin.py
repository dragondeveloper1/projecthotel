from django.contrib import admin
from .models import Roominfo, Packages, Roomdetail

# Register your models here.
class RoomInfo(admin.ModelAdmin):
    class Meta:
        model= Roominfo
admin.site.register(Roominfo,RoomInfo)
class RoomDetail(admin.ModelAdmin):
    class Meta:
        model= Roomdetail
admin.site.register(Roomdetail,RoomDetail)
class Packagesses(admin.ModelAdmin):
    class Meta:
        model= Packages
admin.site.register(Packages,Packagesses)