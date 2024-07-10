from django.shortcuts import render
def home(request):
    factorial=1
    n1=5
    result=fact(n1)
    return render(request,'app1/index.html',{'param1':result,'param2':n1})

def fact(n1):  
    fact1=1
    for i in range(1,n1+1,1):
        fact1=fact1*i
    return fact1
