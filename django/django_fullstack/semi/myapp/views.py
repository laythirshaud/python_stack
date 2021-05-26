from django.shortcuts import redirect, render
from myapp.models import Shows
def inde(request):
    return redirect("/shows")
def index(request):
    context={
        "all_shows" : Shows.objects.all(), 
    }
    return render (request,'index.html',context)
def new(request):
    context={
        "all_shows" : Shows.objects.last(), 
    }
    return render(request,"index2.html",context)
def create(request):
    x=Shows.objects.create(title=request.POST['title'],network=request.POST['network'],relasedate=request.POST['relasedate'],desc=request.POST['desc'])
    request.session["idid"]=request.POST['title']
    return redirect(f"shows/{x.id}")
def index3(request,id):
    cont={
        "all_shows":Shows.objects.get(id=id)
    }
    return render(request,"index3.html",cont)
    
def index4(request,id):
    context={
        "all_shows" : Shows.objects.get(id=id), 
    }
    return render(request,"index4.html",context)
def edit(request):
    new=Shows.objects.get(id=request.POST["hidden"])
    new.title=request.POST['title']
    new.network=request.POST['network']
    new.relasedate=request.POST['relasedate']
    new.desc=request.POST['desc']
    new.save()
    request.session["idid"]=request.POST['title']
    return redirect(f"/shows/{new.id}")
def delete(request,id):
    Shows.objects.get(id=id).delete()
    return redirect("/shows")