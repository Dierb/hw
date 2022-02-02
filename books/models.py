from distutils.command.upload import upload
from pickle import TRUE
from sys import maxunicode
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class BookComment(models.Model):
    books = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="book_comment")
    text = models.TextField()
    creatted_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.books.title
