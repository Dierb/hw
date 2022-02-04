import django
from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

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

class Customuser(User):
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
    
    user_type = models.IntegerField(choices=USER_TYPE, verbose_name="type user", default=client)
    phone = models.CharField(max_length=100)
    age = models.IntegerField()
    genr = models.IntegerField(choices=GEDER_TYPE, verbose_name="gendr")

    
