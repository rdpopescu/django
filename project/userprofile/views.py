import datetime
import random
import string

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import ListView, CreateView

from userprofile.forms import NewAccountForm
from userprofile.models import Pontaj


@login_required
def new_timesheet(request):
    Pontaj.objects.create(user_id=request.user.id,
                          start_date=datetime.datetime.now())
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def stop_timesheet(request):
    Pontaj.objects.filter(user_id=request.user.id, end_date=None).update(end_date=datetime.datetime.now())
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'registration/user_index.html'


class CreateNewAccount(LoginRequiredMixin, CreateView):
    model = User
    template_name = 'forms.html'
    form_class = NewAccountForm

    def get_success_url(self):
        return reverse('userprofile:lista_utilizatori')


def invita_utilizatorul(request, pk):
    psw = "".join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase +
                                               string.digits + '!$%?#@') for _ in range(8))
    if User.objects.filter(id=pk).exists():
        user_instance = User.objects.get(id=pk)
        user_instance.set_password(psw)
        user_instance.save()
        content = f"Datele de autentificare sunt: \n username: {user_instance.username} \n password: {psw}"
        msg_html = render_to_string('registration/invite_user.html', {'content_email': content})
        email = EmailMultiAlternatives(subject='Invitatie utilizator',
                                       body=content,
                                       from_email='contact@test.ro',
                                       to=[user_instance.email])
        email.attach_alternative(msg_html, 'text/html')
        email.send()
    return redirect('userprofile:lista_utilizatori')

