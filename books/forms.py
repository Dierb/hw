from django import forms
from django.forms import fields
from . import models

class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = "__all__"