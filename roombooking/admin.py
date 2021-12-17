from django.contrib import admin
from .models import Roombooking, Eventbooking
# Register your models here.
class RoomBooking(admin.ModelAdmin):
    class Meta:
        model= Roombooking
    list_display= ('category','name')
    search_fields= ['id']
admin.site.register(Roombooking,RoomBooking)

class EventBooking(admin.ModelAdmin):
    class Meta:
        model= Eventbooking
    list_display=('user','event_name','check_in','check_out','persons','comment','payment')
    search_fields= ['user']
admin.site.register(Eventbooking,EventBooking)