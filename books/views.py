
from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.

def hello(request):
    return HttpResponse('hello Kamilla')

def books_all(request):
    books = models.Book.objects.all()
    return render(request, 'book_list.html', {'books':books})
    
