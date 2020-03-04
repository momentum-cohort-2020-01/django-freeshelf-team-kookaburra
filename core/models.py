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
    category = models.ForeignKey(
        'Category', on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return f'Book title: {self.title}'

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
