from django.shortcuts import render

# Create your views here.
def sessy(request):
    sec = int(request.COOKIES.get('count',0))
    newcount = sec+1
    response =  render(request,'sessionapp/session.html',{'count':newcount})
    response.set_cookie('count',newcount)
    return response
