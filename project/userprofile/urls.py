from django.urls import path
from userprofile import views

app_name = 'userprofile'
urlpatterns = [
    path('start_timesheet/', views.new_timesheet, name='start_pontaj'),
    path('stop_timesheet/', views.stop_timesheet, name='oprire_pontaj'),
    path('listare_utilizatori/', views.UserListView.as_view(), name='lista_utilizatori'),
    path("adauga_utilizator/",views.CreateNewAccount.as_view(),name="utilizator_nou"),
    path('<int:pk>/invite/', views.invita_utilizatorul, name='invitatie_utilizator'),
]