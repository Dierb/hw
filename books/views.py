
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from . import models, forms
from django.urls import reverse
from django.views import generic

# Create your views here.

def hello(request):
    return HttpResponse('hello world')

class BooklistView(generic.ListView):
    template_name = "book_list.html"
    QuerySet = models.Book.objects.all()

    def get_queryset(self):
        return self.QuerySet

# def books_all(request):
#     books = models.Book.objects.all()
#     return render(request, 'book_list.html', {'books':books})

class BookDetailView(generic.DetailView):
    template_name ='books_detail.html'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.Book, id=book_id)

# def books_detail(request, id):
#     book = get_object_or_404(models.Book, id = id)
#     return render(request, 'books_detail.html',{'book':book})

class BookAddview(generic.CreateView):
    template_name = 'add_book.html'
    form_class = forms.BookForm
    QuerySet = models.Book.objects.all()
    success_url = "/books/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BookAddview, self).form_valid(form=form)

# def add_book(request):
#     method = request.method
#     if method == 'POST':
#         form = forms.BookForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('book created')
#     else:
#         form = forms.BookForm()
#     return render(request, 'add_book.html', {'form':form})

class BookUpdateView(generic.UpdateView):
    template_name = 'book_update.html'
    form_class = forms.BookForm
    success_url = "/books/"

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.Book, id=book_id)

    def form_valid(self, form):
        return super(BookUpdateView,self).form_valid(form=form)

# def book_update(request, id):
#     book_object = get_object_or_404(models.Book, id=id)
#     if request.method == 'POST':
#         form = forms.BookForm(instance=book_object, data=request.POST)
#         if form.is_valid():
#            form.save()
#         #    return HttpResponse('book updated')
#         return redirect(reverse("books:books_all"))
#     else:
#         form = forms.BookForm(instance=book_object)
#     return render(request, 'book_update.html', {'form': form, 'object': book_object})

class BookdeleteView(generic.DeleteView):
    template_name = "book_delete.html"
    success_url = "/books/"

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.Book, id=book_id)

# def book_delete(request, id):
#     book_object = get_object_or_404(models.Book, id=id)
#     book_object.delete()
#     return HttpResponse('book deleted')


