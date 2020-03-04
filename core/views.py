from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Book, Author, Category, User, Favorite
from .forms import BookForm


# Create your views here.

@login_required
def books_list(request):
    books = Book.objects.order_by('-updated_at')
    favorite_books = get_favorite_books_for_user(request)
    return render(request, 'core/books_list.html', {"books": books, 'favorite_books':favorite_books})

def books_detail(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'core/books_detail.html', {'book': book, 'pk': pk})

def books_by_category(request, slug):
    category = Category.objects.get(slug=slug)
    books_for_category=Book.objects.filter(category=category)
    return render(request, 'core/books_by_category.html', {'books':books_for_category, 'category': category })


#This will prioritize users for the admin.
def get_favorite_books_for_user(request):
    #gets whatever user is making the request
    user = User.objects.get(username=request.user.username)
    #Gets all their favorites aka favorite objects.
    favorite_books = [favorite.book for favorite in user.favorites.all()]
    return favorite_books













# #Code used to help create bookmarks/favorites.
# class BookmarkView(View):
#     # This variable will set the bookmark model to be processed
#     model = None
 
#     def post(self, request, pk):
#         # We need a user
#         user = auth.get_user(request)
#         # Trying to get a bookmark from the table, or create a new one
#         bookmark, created = self.model.objects.get_or_create(user=user, obj_id=pk)
#         # If no new bookmark has been created,
#         # Then we believe that the request was to delete the bookmark
#         if not created:
#             bookmark.delete()
 
#         return HttpResponse(
#             json.dumps({
#                 "result": created,
#                 "count": self.model.objects.filter(obj_id=pk).count()
#             }),
#             content_type="application/json"
#         )

