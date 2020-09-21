from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def welcome(request):
    time=datetime.datetime.now()
    msg = '<h1>hello guys this is my first django application</h1><hr>'
    msg = msg+'<h1> The time is now: '+str(time)+' </h1>'
    return HttpResponse(msg)
