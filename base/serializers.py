from rest_framework import serializers
from .models import *

class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'