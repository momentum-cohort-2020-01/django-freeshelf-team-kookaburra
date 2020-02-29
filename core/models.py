from django.db import models
from django.utils.text import slugify

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tag = models.ForeignKey('Tag', on_delete=models.DO_NOTHING)

#  def __str__(self):
#         return f"Book title: {self.title} description: {self.description}"

class Author(models.Model):
    name = models.CharField(max_length=100)


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=False, unique=True)

    # def __str__(self):
    #         return self.title

    # def get_absolute_url(self):
    #         return reverse('books_detail', args=[str(self.id)])       

    
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.name)
    #     return super().save(*args, **kwargs)
