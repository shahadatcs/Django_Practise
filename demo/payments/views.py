#from django.http import HttpResponse
from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

def home_page(request):
    return render(request,'payments/payments_1.html')
def hom_pag(request):
    return render(request,'payments/payments_2.html')






"""def home_page(request):
    return HttpResponse('Welcome payment') 
def Roket(request):
    return HttpResponse('Payment method ')
def add(request):
   b=30
    z=a+b
    return HttpResponse(z)
def power(request):
    a=2
    b=3
    c=a**b
    return HttpResponse(c)"""