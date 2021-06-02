from django.shortcuts import redirect, render, HttpResponse
import re
from django.contrib import messages
import bcrypt
from . models import Thought, User


def root(request):
    if 'name' in request.session:
        return redirect('/success')
    return render(request,'index.html')

def registration(request):
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    errors = {}
    if len(request.POST["fname"]) < 2:
        errors["fname"] = "First name is too short"

    if len(request.POST["lname"]) < 2:
        errors["lname"] = "Last name is too short"

    if not EMAIL_REGEX.match(request.POST['email']):         
            errors['email'] = "Invalid email address!"

    if len(request.POST["password"]) < 8:
        errors["password"]="short password"

    if request.POST["password"] !=request.POST["confirm"]:
        errors["confirm"]="Not matching"

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('/')
    
    else: 
        first=request.POST['fname']
        last=request.POST['lname']
        em=request.POST['email']
        pas=request.POST["password"]
        conf=request.POST['confirm']
        if pas==conf: #to  make sure its same
            hash = bcrypt.hashpw(pas.encode(), bcrypt.gensalt()).decode()
            user=User.objects.create(first_name=first,last_name=last,email=em,password=hash)

    if 'name' not in request.session:
        request.session['name']=first
        return redirect("/success")
    return redirect("/")

def login(request):

    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    errors1 = {}
    if not EMAIL_REGEX.match(request.POST['lemail']):         
        errors1['lemail'] = "Invalid email address!"
    try:
        oneUser=User.objects.filter(email=request.POST['lemail'])
        errors1['lemaittl'] = "this email does not exist in our data bases!"
    except:
        pass

    if oneUser:
        if bcrypt.checkpw(request.POST["lpassword"].encode(), oneUser[0].password.encode()):
            if 'name' not in request.session:
                    request.session['name']=oneUser[0].first_name
            return redirect("/success")
        else:
            errors1["conf"]="Password Does Not match"

    if len(errors1) > 0:
        for key, value in errors1.items():
            messages.error(request,value)
        return redirect('/')
    return redirect('/')



def success(request):
    if 'name' in request.session:
        someone=User.objects.get(first_name=request.session['name'])
        context={
            'user': someone,
            'all_thoughts' : Thought.objects.all()
        }
        return render(request,'thoughts.html',context)
    return redirect('/')

def logout(request):
    del request.session['name']
    return redirect("/")


def add_thought(request):
    posting=request.POST['addpost']
    someone=User.objects.get(first_name=request.session['name'])
    Thought.objects.create(description=posting,uploade_by=someone)
    return redirect("/")

def thought(request, id):
    this=Thought.objects.filter(id=id)
    this=this[0]
    people_like = User.objects.filter(like=this.id)
    context={
        'this_thought' : this,
        'who_like' : people_like
    }
    return render(request,"show.html",context)

def unlikethought(request, id):
    user_in_session=User.objects.get(first_name=request.session['name'])
    this_thought=Thought.objects.filter(id=id)
    liked_thought=this_thought[0]
    user_in_session.like.remove(liked_thought)
    
    return redirect(f"/thought/{id}")

def likethought(request, id):
    user_in_session=User.objects.get(first_name=request.session['name'])
    this_thought=Thought.objects.filter(id=id)
    liked_thought=this_thought[0]
    user_in_session.like.add(liked_thought)
    return redirect(f"/thought/{id}")