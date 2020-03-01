from django.db import models
from django.utils.text import slugify


class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    author = models.ForeignKey('Author', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING, null=True, blank=True)
    

#  def __str__(self):
#         return f"Book title: {self.title} description: {self.description}"

class Author(models.Model):
    name = models.CharField(max_length=100)


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #         return reverse('books_detail', args=[str(self.id)])       

    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
