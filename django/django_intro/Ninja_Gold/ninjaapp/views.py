from django.shortcuts import redirect, render, HttpResponse
import random
from time import gmtime, strftime
def index(request):
    request.session['value']=0
    return render(request,'index.html')
def index2(request):
    return render(request,'index2.html')
def find(request):
    request.session['gold']=random.randint(10,20)
    request.session['gold1']=random.randint(5,10)
    request.session['time']=strftime("%Y-%m-%d %H:%M %p", gmtime())
    request.session['time1']=strftime("%Y-%m-%d %H:%M %p", gmtime())
    return redirect('/index2')

# def cave(request):
#     request.session['gold1']=random.randint(5,10)
#     request.session['time1']=strftime("%Y-%m-%d %H:%M %p", gmtime())
#     return redirect('/index2')

# def find(request):
#     request.session['gold']=random.randint(2,5)
#     request.session['time']=strftime("%Y-%m-%d %H:%M %p", gmtime())
#     return redirect('/index2')


