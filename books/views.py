
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from . import models, forms
from django.urls import reverse

# Create your views here.

def hello(request):
    return HttpResponse('hello Kamilla')

def books_all(request):
    books = models.Book.objects.all()
    return render(request, 'book_list.html', {'books':books})

def books_detail(request, id):
    book = get_object_or_404(models.Book, id = id)
    return render(request, 'books_detail.html',{'book':book})

def add_book(request):
    method = request.method
    if method == 'POST':
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('book created')
    else:
        form = forms.BookForm()
    return render(request, 'add_book.html', {'form':form})

def book_update(request, id):
    book_object = get_object_or_404(models.Book, id=id)
    if request.method == 'POST':
        form = forms.BookForm(instance=book_object, data=request.POST)
        if form.is_valid():
           form.save()
        #    return HttpResponse('book updated')
        return redirect(reverse("books:books_all"))
    else:
        form = forms.BookForm(instance=book_object)
    return render(request, 'book_update.html', {'form': form, 'object': book_object})

def book_delete(request, id):
    book_object = get_object_or_404(models.Book, id=id)
    book_object.delete()
    return HttpResponse('book deleted')


