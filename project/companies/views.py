from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView, ListView

from companies.forms import CompanyForm
from companies.models import Company


class CreateCompaniesView(LoginRequiredMixin, CreateView):
    model = Company
    form_class = CompanyForm
    template_name = 'forms.html'

    def get_success_url(self):
        return reverse('companies:lista_companii')


class CompaniesView(LoginRequiredMixin, ListView):
    model = Company
    template_name = 'companies/index.html'