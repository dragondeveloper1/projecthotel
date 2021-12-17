from django.db import models
from loginapi.models import CustomUser
from roominfoapi.models import  Roominfo,Roomdetail,Packages
from django.conf import settings
from datetime import datetime
import pytz


# Create your models here.
class Roombooking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category= models.ForeignKey(Roominfo, on_delete=models.CASCADE)
    name = models.ForeignKey(Roomdetail, on_delete=models.CASCADE)
    check_in= models.DateTimeField()
    check_out= models.DateTimeField()
    # has_checked_out= models.BooleanField(null=True,blank=True)

    def filter_booking(self,checkindate,checkoutdate,roomtype):
        print(checkindate)
        print(checkoutdate)
        print(roomtype)
        my_booking = Roombooking.objects.all()
        print(my_booking)
        epoch = datetime.utcfromtimestamp(0)
        for i in my_booking:
            print(type(i.check_out))
            print(type(checkindate))
            dt = datetime.fromisoformat(checkindate)
            now_aware = dt.replace(tzinfo=pytz.Asia/Kathmandu)
            CheckInDate= (now_aware - epoch).total_seconds() * 1000.0
            print(CheckInDate)
            check_out = (i.check_out-epoch).total_seconds()*1000.0
            if check_out < CheckInDate or i.check_out > checkin:
                print(my_booking)
        return my_booking


class Eventbooking(models.Model):
    payment_choices=(
        ("card","Card"),
        ("online","Online"),
        ("cheque", "Cheque"),
        ("cash", "Cash"),
        ("others", "Others"),
    )
    user= models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    event_name= models.CharField(max_length=250)
    title= models.ForeignKey(Packages, on_delete=models.CASCADE)
    check_in= models.DateTimeField()
    check_out= models.DateTimeField()
    persons= models.IntegerField()
    comment= models.CharField(max_length=1000)
    payment= models.CharField(max_length=25, choices=payment_choices, default="card")
    
    def __self__(self):
        return self.title+self.event_name