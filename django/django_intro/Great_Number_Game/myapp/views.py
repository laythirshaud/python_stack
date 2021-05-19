from django.shortcuts import redirect, render, HttpResponse
import random
def check(request):
    request.session['number']=random.randint(1, 100)
    return render(request,'home.html')

def result(request):
    usernumber =int(request.POST['box'])
    if usernumber < request.session['number'] :
        request.session['com']="too low"
        return render(request,'index.html')
    elif usernumber > request.session['number'] :
        request.session['com']="too high"
        return render(request,'index.html')
    else :
        request.session['com']="you are correct"
        return render(request,'index2.html')

def delete(request):
    request.session.clear
    return redirect('/')



