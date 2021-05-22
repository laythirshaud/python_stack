from django.shortcuts import redirect, render, HttpResponse
import random
from time import gmtime, strftime
def index(request):
    if 'gold' not in request.session:
        request.session['gold']=0
    if "act" not in request.session:
        request.session['act']=[]
        act = request.session['act']
    else:
        act = request.session['act']

    context={
        'act' :act
    }

    return render(request, 'index.html' , context)




def index2(request):
    time = strftime("%Y-%m-%d %H:%M %p", gmtime())

    if request.POST["hidden"]=="farm":
        gold=random.randint(10,20)
        request.session['act'].append( f"Earned {gold} from the farm {time}" )
    if 'value' not in request.session:
        request.session['value']=0
    elif request.POST["hidden"]=="cave":
        gold=random.randint(5,10)
        request.session['act'].append( f"Earned {gold} from the cave {time}" )
    if 'value' not in request.session:
        request.session['value']=0
    elif request.POST["hidden"]=="house":
        gold=random.randint(5,10)
        request.session['act'].append( f"Earned {gold} from the house {time}" )
    if 'value' not in request.session:
        request.session['value']=0
    elif request.POST["hidden"]=="casino":
        gold=random.randint(-50,50)
        if gold < 0 :
            request.session['act'].append( f"lost {gold} from the casino {time}" )
        else:
            request.session['act'].append( f"Earned {gold} from the casino {time}" )
    request.session['gold']+=gold
    return redirect('/')



def updat(request):
    request.session.clear()
    return redirect("/")