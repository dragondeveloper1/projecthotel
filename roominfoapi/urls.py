from django.urls import path
from rest_framework.routers import DefaultRouter
from roominfoapi.views import Roominfo_viewSet, Roomdetail_viewSet,Packages_viewSet
# from .views import PostList, PostDetail
app_name = 'roominfoapi'
router = DefaultRouter()
router.register('Roominfo', Roominfo_viewSet, basename='roominfo')
router.register('Roomdetail', Roomdetail_viewSet, basename='roomdetail')
router.register('Packages', Packages_viewSet, basename='packages')

urlpatterns = [

]
urlpatterns+= router.urls