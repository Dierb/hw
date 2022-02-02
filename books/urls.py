
from django.urls import path
from . import views

app_name = 'books'
urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('books/', views.BooklistView.as_view(), name='books_all'),
    path('books/<int:id>/', views.BookDetailView.as_view(), name='books_detail'),
    path('books/<int:id>/update/', views.BookUpdateView.as_view(), name='book_apdate'),
    path('books/<int:id>/delete/', views.BookdeleteView.as_view(), name='book_delete'),
    path('add-book/', views.BookAddview.as_view(), name='add_book'),
]
