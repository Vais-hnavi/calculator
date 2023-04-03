from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def calc(request):
    return render(request,"calc.html",{"name":"vaishnavi"})

def add(request):
    n1= int(request.POST["num1"])
    n2= int(request.POST["num2"])
    op=str(request.POST["op"])
    if request.method =="POST":
        if op == "+":
            res = n1+n2
        elif op == "-":
            res= n1-n2
        elif op == "*":
            res = n1*n2
        elif op =="/":
            res= n1/n2
        else:
            messages.error(request,'Invalid Operator')
            return render(request,"result.html",{'result':'Enter a valid operator'})
        return render(request,'result.html',{'result':res})
