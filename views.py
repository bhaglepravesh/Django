from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
import datetime


# Create your views here.

def display(request):
    return HttpResponse("<h1> My first django app!</h1>")


def displaydatetime(request):
    dt=datetime.datetime.now()
    s="<br> Current date and time is: </br>"+str(dt)
    
    return HttpResponse(s)