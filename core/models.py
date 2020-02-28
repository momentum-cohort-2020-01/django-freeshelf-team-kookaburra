from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('Author', on_delete=models.DO_NOTHING)

# We will not need this.
class Author(models.Model):
    name = models.CharField(max_length=100)
