from django.http import HttpResponse
from django.shortcuts import render
from. models import Place
from. models import Testimonials

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj1=Testimonials.objects.all()
    return render(request,'index.html',{'result':obj,'result1':obj1})




# def subtraction(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x-y
#     return render(request,"result.html",{'result':res})
# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res1=x+y
#     return render(request,"result1.html",{'result1':res1})
