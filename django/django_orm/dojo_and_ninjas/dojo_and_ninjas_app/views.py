from dojo_and_ninjas_app.models import dojo, ninja
from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    context = {
        "dojos": dojo.objects.all(),
    }
    return render(request , 'index.html',context)

def srap(request):
    if request.method == 'POST':
        dojo.objects.create(name=request.POST["name"],city=request.POST["city"],state=request.POST["state"])
    return redirect('/')
def secand(request):
    ninja.objects.create(first_name=request.POST["first_name"],last_name=request.POST["last_name"],dojo_id= dojo.objects.get(id= int(request.POST["dojo_id"])))
    return redirect('/')