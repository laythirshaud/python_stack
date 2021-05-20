from django.shortcuts import render, HttpResponse,redirect
def index(request):
    context = {
        "user": user.objects.all()
    }
    return render(request, "index.html", context)

from .models import user
def result(request):
    user.objects.create(first_name =request.POST["first_name"],secand_name =request.POST["secand_name"],email_address =request.POST["email_address"],age =request.POST["age"])
    return redirect("/")