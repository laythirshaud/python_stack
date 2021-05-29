from django.shortcuts import redirect, render, HttpResponse
from . models import User
import re
from django.contrib import messages
import bcrypt
def root(request):
    return render(request, 'index.html')

# def home(request):
#     if "user_id" not in request.session:
#         return redirect('/')
#     user=User.objects.get(id=request.session['user_id'])
#     return render(request ,'homepage.html',{
#         'name': user.first_name +" " + user.last_name
#     })

def registration(request):
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    errors = {}
    if len(request.POST['fname']) < 2:
        errors["fname"]="first-name is too short"

    if len(request.POST['lname']) < 2:
        errors["lname"]="last-name is too short"

    if not EMAIL_REGEX.match(request.POST['email']):          
        errors['email'] = "Invalid email address!"

    if len(request.POST['password']) < 8:
        errors['password']='short password'
       
    if request.POST["password"] != request.POST["confirm"]:
        errors["confirm"]="NOT matching"
    for key, value in errors.items():
        if len(errors)> 0:
            messages.error(request,value)
            return redirect("/")
    else:
        first = request.POST['fname'],
        last = request.POST['lname'],
        em = request.POST['email'],
        password = request.POST['password'],
        conf = request.POST['confirm'],
        if password==conf:
            hash = bcrypt.hashpw('password'.encode(), bcrypt.gensalt()).decode()
            print("!!!!!!!!!!!!!!!!!!!111")
            User.objects.create(first_name=first,last_name=last,email=em,password=hash)
            if 'name' not in request.session:
                request.session['name']=first
            return redirect("/success")
        return redirect('/')

def success(request):
    return render(request,'success.html')

def logout(request):
    del request.session['name']
    return redirect("/")





# def logout(request):
    











