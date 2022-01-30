
from django.urls import path
from . import views

app_name = 'books'
urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('books/', views.books_all, name='books_all'),
    path('books/<int:id>/', views.books_detail, name='books_detail'),
    path('books/<int:id>/update/', views.book_update, name='book_apdate'),
    path('books/<int:id>/delete/', views.book_delete, name='book_delete'),
    path('add-book/', views.add_book, name='add_book'),
    
]
