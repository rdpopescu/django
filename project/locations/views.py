from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from locations.forms import LocationsForm
from locations.models import Location


class CreateLocationView(CreateView):
    model = Location
    template_name = "forms.html"
    # fields = ["city", "country"]
    form_class = LocationsForm

    def get_form_kwargs(self):
        data = super(CreateLocationView, self).get_form_kwargs()
        data.update({'pk': None})
        return data


    def get_success_url(self):
        return reverse("locations:lista_locatii")

class LocationView(ListView):
    model = Location
    template_name="locations/location_index.html"


class UpdateLocationView(UpdateView):
    model = Location
    # fields = ['city','country']
    form_class = LocationsForm
    template_name = "forms.html"

    def get_form_kwargs(self):
        data = super(UpdateLocationView, self).get_form_kwargs()
        data.update({'pk': self.kwargs['pk']})
        return data

    def get_success_url(self):
        return reverse("locations:lista_locatii")


def deactivate_location(request, pk):
    Location.objects.filter(id=pk).update(active=False)
    return redirect("locations:lista_locatii")


def activate_location(request, pk):
    Location.objects.filter(id=pk).update(active=True)
    return redirect("locations:lista_locatii")
