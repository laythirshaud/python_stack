from books_authors_app.models import Book, outhor
from django.shortcuts import redirect, render, HttpResponse
def index(request):
    context = {
        "book": Book.objects.all()
    }
    return render(request, 'index.html', context)

def show(request):
    tit= request.POST['title']
    des= request.POST['desc']
    Book.objects.create(title=tit, desc=des)
    return redirect('/')

def view(request,id):
    context = {
        "book": Book.objects.get(id=id),
        "outhor": outhor.objects.all()
    }
    return render(request, 'index2.html', context)

def add(request):
    x = request.POST['name']
    # "book": Book.objects.get()
    book=Book.add(x)
    return redirect('index2.html')