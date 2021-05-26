from django.shortcuts import redirect, render
from . import models
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