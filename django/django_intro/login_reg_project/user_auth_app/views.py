from django.shortcuts import redirect, render, HttpResponse 
from user_auth_app.models import User

def index(request):
    if 'user' in request.session:
        return redirect('/welcome')
    return render(request,'index.html')

def login(request):
    username =request.POST['username']
    passwd =request.POST['passwd']
    
    users =User.objects.filter(username = username)
    if len(users) ==0:
        return redirect('/')
    user =users.first()
    if  user.password != passwd:
        return redirect('/')
    data={
        "username":user.username,
        "password":user.password,
        "address":user.address,
        "email":user.email
    }
    request.session['user'] = data
    return redirect("/welcome")

def regester(request):
    username =request.POST['username']
    passwd =request.POST['passwd']
    address =request.POST['address']
    email=request.POST['email']
    user= User.objects.create(username=username, password=passwd, email=email, address=address)
    data={
        "username": username,
        "password":passwd,
        "address":address,
        "email":email
    }
    
    request.session['user'] = data
    return redirect("/welcome")
    
def welcome(request):
    if 'user' in request.session:
        data= request.session['user']
        return render(request, "welcome.html", data)
    return redirect('/')

def logout(request):
    if 'user' in request.session:
        request.session.clear()
        return redirect('/')
    return redirect('/')
