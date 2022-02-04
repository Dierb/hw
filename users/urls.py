from django.contrib.auth.forms import AuthenticationForm
from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('register/', views.Registration.as_view(), name='registration'),
    path('login/', views.Newloginview.as_view(), name='login'),
    path('user/', views.Userlistview.as_view(), name='user_list'),
]