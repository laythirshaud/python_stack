from django.db import models
class Book(models.Model):
    title = models.CharField(max_length=255)
    desc =models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    notes =models.TextField()
    books = models.ManyToManyField(Book, related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def addOneBook(title, desc):
    new_book= Book.objects.create(title=title, desc=desc)
    return new_book

def allBooks():
    return Book.objects.all()

def getBook(id):
    return Book.objects.get(id=id)
def allAuthors():
    return Author.objects.all()

def allAuthor():
    return Author.objects.all()