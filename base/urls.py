from django.urls import include, path
from .views import *
from rest_framework import routers
from base import views

router = routers.DefaultRouter()
router.register(r'city', views.CityViewSet)
router.register(r'hotel', views.HotelViewSet)

urlpatterns = [
    path('router', include(router.urls)),
    path('api/auth', include('rest_framework.urls', namespace='rest_framework')),
    path('', Index.as_view(), name='index'),
    path('stad/<str:city_name>', Stad.as_view(), name='stad'),
    path('hotels/', HotelDetail.as_view(), name='hotel'),
]