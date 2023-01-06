#from http.client import HTTPResponse
from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def ngo(request):
    return render(request,'Aunthentication/Aunthentication_1.html')
    #return HTTPResponse('Shahadat Hossain')