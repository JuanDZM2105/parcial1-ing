from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from django.db.models import Avg
from .models import Flight

# Vista de inicio
class HomePageView(TemplateView):
    template_name = 'vuelos/home.html'

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['name', 'flight_type', 'price']
        widgets = {
            'flight_type': forms.Select(choices=Flight.flightTypes)
        }

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError('El precio debe ser mayor que cero.')
        return price
    
class FlightRegisterView(TemplateView):
    template_name = 'vuelos/register.html'

    def get(self, request):
        form = FlightForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_flights')
        return render(request, self.template_name, {'form': form})

class FlightListView(ListView):
    model = Flight
    template_name = 'vuelos/list.html'
    context_object_name = 'flights'
    ordering = ['price']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "List of Flights"
        return context

class FlightStatisticsView(TemplateView):
    template_name = 'vuelos/stats.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Flight Statistics"
        context["total_national"] = Flight.objects.filter(flight_type="Nacional").count()
        context["total_international"] = Flight.objects.filter(flight_type="Internacional").count()
        context["avg_price_national"] = Flight.objects.filter(flight_type="Nacional").aggregate(Avg('price'))['price__avg'] or 0
        return context