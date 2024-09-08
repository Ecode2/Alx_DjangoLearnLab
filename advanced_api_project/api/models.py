from django.db import models

# Create your models here.

## Model for author of a book
class Author(models.Model):
    name=models.CharField(max_length=100)


## Model for books with a foreign key relating to the author 
class Book(models.Model):
    title=models.CharField(max_length=100)
    publication_year=models.IntegerField()
    author=models.ForeignKey(to=Author, related_name="books", on_delete=models.CASCADE)