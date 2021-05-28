from django.shortcuts import redirect, render
from . import models
from .models import Book, Author
def index(request):
    context={
        'books' : models.allBooks()
    }
    return render(request, 'books.html',context)

def addBook(request):
    if request.method =='POST':
        title=request.POST['title']
        decs=request.POST['desc']
        newly_created_book=models.addOneBook(title, decs)
        return redirect('/')

def showBook(request, id):
    context ={
        'this_book':models.getBook(id),
        'allAuthors':models.allAuthors()
    }
    return render(request, "showBook.html", context)
def addAuthorToBook(request,book_id):
    selected_author_id= request.POST['selected_author']
    selected_author=models.Author.objects.get(id=selected_author_id)
    this_book =models.Book.objects.get(id=book_id)
    this_book.authors.add(selected_author)
    return redirect(f'/books/{book_id}')

def index2(request):
    context={
        'authors': models.allAuthor()
    }
    return render(request,'Authors.html',context)

def addAuthor(request):
    if request.method =='POST':
        first_name=request.POST['firstName']
        last_name=request.POST['lastName']
        notes=request.POST['notes']
        models.Author.objects.create(first_name=first_name,last_name=last_name, notes=notes )
        return redirect('/authors')
def showauthor(request,id):
    context={
        'this_author': models.Author.objects.get(id=id) ,
        'books':models. allBooks()
    }
    return render(request ,'showAuthor.html', context)

def add_book_to_author(request, author_id):
    author = Author.objects.get(id=author_id)
    book = Book.objects.get(id=request.POST['book_id'])
    author.books.add(book)
    return redirect(f'/authors/{author_id}')