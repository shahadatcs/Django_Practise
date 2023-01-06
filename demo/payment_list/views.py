from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def pay(request):
    return render(request,'payment_list/payment_list.html')
