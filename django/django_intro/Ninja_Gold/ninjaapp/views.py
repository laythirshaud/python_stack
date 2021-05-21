from django.shortcuts import redirect, render, HttpResponse
import random
# from time import gmtime, strftime
def index(request):
    if 'value' not in request.session:
        request.session['value']=0
    else:
        if request.POST["hidden"]=="farm":
            request.session['gold']+=random.randint(10,20)
    if 'value' not in request.session:
        request.session['value']=0
    else:
        if request.POST["hidden"]=="cave":
            request.session['gold']+=random.randint(5,10)
    if 'value' not in request.session:
        request.session['value']=0
    else:
        if request.POST["hidden"]=="house":
            request.session['gold']+=random.randint(5,10)
    if 'value' not in request.session:
        request.session['value']=0
    else:
        if request.POST["hidden"]=="casino":
            request.session['gold']+=random.randint(0,50)
    return render(request, 'index.html')
# def index2(request):
#     return render(request,'index2.html')
# def find(request):
#     request.session['gold']=random.randint(10,20)
#     request.session['gold1']=random.randint(5,10)
#     request.session['time']=strftime("%Y-%m-%d %H:%M %p", gmtime())
#     request.session['time1']=strftime("%Y-%m-%d %H:%M %p", gmtime())
#     return redirect('/index2')

# def cave(request):
#     request.session['gold1']=random.randint(5,10)
#     request.session['time1']=strftime("%Y-%m-%d %H:%M %p", gmtime())
#     return redirect('/index2')

# def find(request):
#     request.session['gold']=random.randint(2,5)
#     request.session['time']=strftime("%Y-%m-%d %H:%M %p", gmtime())
#     return redirect('/index2')


