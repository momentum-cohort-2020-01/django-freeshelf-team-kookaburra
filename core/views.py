from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

# Create your views here.
from .models import Book
from .models import Author

def books_list(request):
    books = Book.objects.all()
    return render(request, 'core/books_list.html', {'books': books})

def books_detail(reqest, pk):
    book = Book.onjects.get(pk=pk)
    return render(request, 'core/books_detail.html', {'book': book, 'pk': pk})




