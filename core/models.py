from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Book(models.Model):
    
    title = models.ForeignKey('Title', on_delete=models.DO_NOTHING)
    description = models.TextField(max_length=1000)
    author = models.ForeignKey('Author', on_delete=models.DO_NOTHING)
    published = models.DateField(auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='core/images/')
    url = models.URLField(blank=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    # def __str__(self):
    #     return f'{self.name}'

    def __str__(self):
        return f"Book title: {self.title} description: {self.description}"
    

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

class Title(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.name  

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

#Step 4 We do a CASCADE so that if the user delete's their profile it deletes everything about the user, not just one thing.
class Favorite(models.Model):
    Favorite = models.ForeignKey(User, related_name="favorites", on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name="favorites", on_delete=models.CASCADE)

    def __str__(self):
        return f'Favorite: {self.favorite}, Book: {self.book}'
    