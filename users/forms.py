from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.db.models import fields

from users import models

ADMIN = 1
VIPclient = 2
client = 3
USER_TYPE = (
    (ADMIN, 'ADMIN'),
    (VIPclient, 'VIP-client'),
    (client, 'client')
)
male = 1
female = 2
GEDER_TYPE = (
    (male, 'male'),
    (female, 'female')
)

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    user_type = forms.ChoiceField(choices=USER_TYPE, required=True)
    genr = forms.ChoiceField(choices=GEDER_TYPE, required=True)

    class Meta:
        model = models.Customuser
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "age",
            'user_type',
            "genr"
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm,self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs=
        {'class': 'form-control',
        'placeholder' : "username" ,
        "id" : "hello"}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs=
        {'class': 'form-control',
        'placeholder' : "password" ,
        "id" : "hi"}
    ))

