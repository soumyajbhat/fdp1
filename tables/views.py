from django.shortcuts import render
from tables.forms import inputweb
from itertools import permutations

def home(request):

 
    if request.method=="POST":
        result=1
        n1=1
        form1=inputweb(request.POST)
        if form1.is_valid():
            data=form1.cleaned_data
            n1=data.get("input1")
            n2=data.get("input2")
            result=fact(n1,n2)
            return render(request,"tables/index.html",{'param1':result, 'param2':n1, 'form':form1})
    else:
        result=1
        n1=1
        form1=inputweb()      
        return render(request,"tables/index.html",{'param1':result, 'param2':n1, 'form':form1})
    
def fact(n1,n2):  
    res=[]
    for n in range(n1,n2+1):
        for x in range(1,11):
            s=n*x
            res.append(s)
           
    
    
    return res  
# Create your views here.
