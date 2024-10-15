from django import forms
from django.forms import TextInput

from locations.models import Location


class LocationsForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['city', 'country']

        widgets = {
            'city': TextInput(attrs={'class': 'form-control', 'placeholder': 'city'}),
            'country': TextInput(attrs={'class': 'form-control', 'placeholder': 'country'})
        }


    def __init__(self, pk, *args, **kwargs):
        super(LocationsForm, self).__init__(*args, **kwargs)
        self.pk=pk

    def clean(self):
        city_value = self.cleaned_data.get('city')
        country_value = self.cleaned_data.get('country')
        if self.pk:
            if Location.objects.filter(city=city_value,
                                       country=country_value).exclude(id=self.pk).exists():
                self._errors['city'] = self.error_class(['Orasul si tara deja exista'])
        else:
            if Location.objects.filter(city=city_value, country=country_value).exists():
                self._errors['city'] = self.error_class(['Orasul si tara deja exista'])
        return self.cleaned_data