
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from . import models

# Create your views here.

def hello(request):
    return HttpResponse('hello Kamilla')

def books_all(request):
    books = models.Book.objects.all()
    return render(request, 'book_list.html', {'books':books})

def books_detail(request, id):
    book = get_object_or_404(models.Book, id = id)
    return render(request, 'books_detail.html',{'book':book})
