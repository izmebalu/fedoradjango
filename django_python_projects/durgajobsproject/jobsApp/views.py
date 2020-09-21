from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def mumbai(request):
    s = '<h1> These are mumbai jobs </h1>'
    return HttpResponse(s)

def pune(request):
    s = '<h1> These are pune jobs </h1>'
    return HttpResponse(s)

def hyd(request):
    s = '<h1> These are hyd jobs </h1>'
    return HttpResponse(s)
