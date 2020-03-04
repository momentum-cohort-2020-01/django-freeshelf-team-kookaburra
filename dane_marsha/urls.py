"""dane_marsha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from core import views

from django.conf.urls import url
from django.contrib.auth.decorators import login_required



urlpatterns = [
    path('accounts/', include('registration.backends.default.urls')),
    path('', views.books_list, name='books_list'),
    path('books/<int:pk>', views.books_detail, name='books_detail'),
    path('books/<slug:slug>/', views.books_by_category, name='books_by_category'),
    # path('', include('books.urls')),
    path('admin/', admin.site.urls),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)













# #Code used to help create bookmarks/favorites.
# from . import views
# from .models import BookmarkArticle, BookmarkComment
 
# app_name = 'ajax'
# urlpatterns = [
#     url(r'^article/(?P<pk>\d+)/bookmark/$',
#         login_required(views.BookmarkView.as_view(model=BookmarkArticle)),
#         name='article_bookmark'),
#     url(r'^comment/(?P<pk>\d+)/bookmark/$',
#         login_required(views.BookmarkView.as_view(model=BookmarkComment)),
#         name='comment_bookmark'),
# ]
