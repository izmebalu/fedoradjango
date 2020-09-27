from django.shortcuts import render
'''from django.http import HttpResponse

# Create your views here.
def mumbai(request):
    s = "<h1>This is mumbai job</h1>"
    return HttpResponse(s)
def pune(request):
    s = "<h1>This is pune job</h1>"
    return HttpResponse(s)
def chennai(request):
    s = "<h1>This is chennai job</h1>"
    return HttpResponse(s)'''
def tempview(request):
    return render(request,'jobsampleApp/wish.html')
