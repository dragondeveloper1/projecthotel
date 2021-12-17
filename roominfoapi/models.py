from django.db import models
# from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Roominfo(models.Model):
    category= models.CharField(max_length=250, default="delux", unique=True)
    img= models.ImageField(upload_to="media")
    def __str__(self):
        return self.category
        
    
class Roomdetail(models.Model):
    name = models.CharField(max_length=250, unique=True)
    category= models.ForeignKey(Roominfo, on_delete=models.CASCADE)
    img= models.ImageField(upload_to ="media")
    img1= models.ImageField(upload_to="media")
    img2 = models.ImageField(upload_to="media")
    slug= models.SlugField(max_length=200)
    capacity= models.IntegerField(default=1, blank=True, null=True)
    price= models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    room_detail= models.CharField(max_length=10000)
    published = models.DateTimeField()
    updated_on= models.DateTimeField(blank=True, null=True )
    #status = models.CharField(max_length=30, choices=room_choices)
    is_booked= models.BooleanField(null=True,blank=True)

    def __str__(self):
        return self.name

class Packages(models.Model):
    title= models.CharField(max_length=200,unique=True)
    #events= models.ForeignKey(Category,on_delete=models.CASCADE)
    slug=models.SlugField(max_length=250)
    img= models.ImageField(upload_to="media")
    img1= models.ImageField(upload_to="media")
    img2= models.ImageField(upload_to="media")
    package_detail= models.CharField(max_length=10000)
    price= models.DecimalField(max_digits=10, decimal_places=2,null=False)
    created_on = models.DateTimeField()
    updated_on= models.DateTimeField()
    status= models.CharField(max_length=10)
    def __str__(self):
        return self.title