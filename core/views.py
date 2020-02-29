from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

# Create your views here.
from .models import Book, Tag
from .models import Author

def books_list(request):
    books = Book.objects.all('-created_at')
    return render(request, 'core/books_list.html', {'books': books})

def books_detail(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'core/books_detail.html', {'book': book, 'pk': pk})

def books_by_tag(request, slug):
    tag = Tag.objects.get(slug=slug)
    books_for_tag=Book.objects.filter(tag=tag)
    return render(request, 'core/books_by_tag.html', {'books':books_for_tag, 'tag': tag })



