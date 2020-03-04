from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login
from .models import Book, Category
from .models import Author

def registeruser(request):
    if request.method == 'GET':
        return render (request, 'core/registeruser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('books_list')

            except IntegrityError:
                return render (request, 'core/registeruser.html', {'form':UserCreationForm(), 'error':'That username is already taken.  Please select a different username.'})

        else:
            return render (request, 'core/registeruser.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})



def books_list(request):
    books = Book.objects.all()
    return render(request, 'core/books_list.html', {'books': books})

def books_detail(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'core/books_detail.html', {'book': book, 'pk': pk})

def books_by_category(request, slug):
    category = Category.objects.get(slug=slug)
    books_for_category=Book.objects.filter(category=category)
    return render(request, 'core/books_by_category.html', {'books':books_for_category, 'category': category })



