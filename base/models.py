from django.db import models
from cms.models.pluginmodel import CMSPlugin
# Create your models here.
# Hier maak ik een database model aan met de naam Data.
# Toen ik nog een noob was ↑
class City(models.Model):
    city_id = models.CharField(max_length=100)
    city_name = models.CharField(max_length=100)

    def __str__(self):
        return self.city_name

class Hotel(models.Model):
    city = models.ForeignKey(City, related_name='test', on_delete=models.CASCADE)
    hotel_id = models.CharField(max_length=100)
    hotel_name = models.CharField(max_length=100)

    def __str__(self):
        return self.hotel_name

class HelloPluginModel(CMSPlugin):
    hotel = models.ForeignKey(Hotel, related_name='pluginmodel', on_delete=models.CASCADE)
    text = models.CharField(max_length=256)
    
    def __str__(self):
        return self.text