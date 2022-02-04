from django.http.request import QueryDict
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, ListView
from django.urls import reverse
from . import models
from users.forms import LoginForm, RegistrationForm

class Registration(CreateView):
    queryset = models.Customuser.objects.all()
    form_class = RegistrationForm
    success_url = '/user/'
    template_name = 'registration.html'

    def get_success_url(self) -> str:
        return super().get_success_url()

class Newloginview(LoginView):
    form_class = LoginForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse('users:user_list')

class Userlistview(ListView):
    Queryset = User.objects.all()
    template_name = 'user_list.html'

    def get_queryset(self):
        return User.objects.all()
