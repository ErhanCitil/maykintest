from .models import Data
from django.views import generic
from .forms import FormContact
from django.urls import reverse_lazy
# Create your views here.

class Index(generic.ListView):
    model = Data
    template_name = 'index.html'
    context_object_name = 'data'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = Data.objects.values('city_name').distinct()
        return context

# Class-Based View voor de stad pagina ik geef de stad naam mee als parameter. Altijd met een hoofdletter de naam van een class
class Stad(generic.CreateView):
    model = Data
    fields = ['city_name']
    template_name = 'stad.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = Data.objects.filter(city_name=self.kwargs['city_name'])
        return context

class ContactSave(generic.FormView):
    template_name = 'contact.html'
    form_class = FormContact
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class Hotel(generic.ListView):
    model = Data
    template_name = 'hotels.html'
    context_object_name = 'data'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = Data.objects.values('city_name').distinct()
        return context