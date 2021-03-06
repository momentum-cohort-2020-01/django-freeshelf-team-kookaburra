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

urlpatterns = [
    path('', views.books_list, name='books_list'),
    path('books/<int:pk>', views.books_detail, name='books_detail'),
    path('books/<slug:slug>/', views.books_by_category, name='books_by_category'),
    # path('', include('books.urls')),
    path('admin/', admin.site.urls),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
