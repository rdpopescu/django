from django.urls import path
from django.urls import path
from companies import views

app_name = 'companies'

urlpatterns = [
    path('adaugare/', views.CreateCompaniesView.as_view(), name='adaugare_companie'),
    path('', views.CompaniesView.as_view(), name='lista_companii'),
]