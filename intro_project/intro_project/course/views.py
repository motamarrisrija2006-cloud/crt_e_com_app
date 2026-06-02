from django.shortcuts import render

# Create your views here.
#http: // 127.0.0.1: 8000 /user/message
from django.http import HttpResponse
def greet(request):
    return HttpResponse("Hii, good morning!")
def get_name(request):
    return HttpResponse("my name is srija")
