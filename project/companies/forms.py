from django import forms
from django.forms import TextInput, ChoiceField, ModelChoiceField, Select

from companies.models import Company
from locations.models import Location


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'

        widgets = {
            'name': TextInput(attrs={'placeholder': 'name', 'class': 'form-control'}),
            'website': TextInput(attrs={'placeholder': 'website', 'class': 'form-control'}),
            'company_type': Select(attrs={'class': 'form-control'}),
            'location': Select(attrs={'class': 'form-control'})
        }