from django.contrib import admin
from django.db import models
from . import models

# Register your models here.

admin.site.register(models.Tag)
admin.site.register(models.Product)
admin.site.register(models.Order)
admin.site.register(models.Customer)


