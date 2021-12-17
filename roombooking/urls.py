from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import Roombooking_viewSet,Eventbooking_viewSet, AvailableRoom
# from .views import PostList, PostDetail
app_name = 'roombookingapi'
router = DefaultRouter()
router.register('Roombooking', Roombooking_viewSet, basename='roombooking')
router.register('Eventbooking', Eventbooking_viewSet, basename='eventbooking')
router.register('availableroom',AvailableRoom, basename="availableroom")
urlpatterns = [

]
urlpatterns+= router.urls