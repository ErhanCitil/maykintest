from .models import *
from django.views import generic
from rest_framework import viewsets
from .serializers import *
from rest_framework import permissions
from rest_framework import generics
import requests
# Create your views here.

class Index(generic.ListView):
    model = City
    template_name = 'index.html'
    context_object_name = 'data'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = City.objects.values('city_name').distinct()
        return context

# Class-Based View voor de stad pagina ik geef de stad naam mee als parameter. Altijd met een hoofdletter de naam van een class
class Stad(generic.ListView):
    model = Hotel
    template_name = 'stad.html'
    context_object_name = 'data'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = Hotel.objects.filter(city__city_name=self.kwargs['city_name'])
        return context

class HotelDetail(generic.ListView):
    model = City
    template_name = 'hotels.html'
    context_object_name = 'data'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = City.objects.values('city_name').distinct()
        return context

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_api_data(self, request):
        request = requests.get('http://routercity')
        return request.json()

class HotelViewSet(generics.DestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return Hotel.objects.get(id=self.kwargs['id'])
