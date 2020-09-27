from django.shortcuts import render
import datetime
# Create your views here.
def homing(request):
    date = datetime.datetime.now()
    msg = ''
    h = int(date.strftime('%H'))
    if h<12:
        msg = "Good Morning"
    elif h<16:
        msg = "Good afternoon"
    elif h<21:
        msg = "Good evening"
    else:
        msg = "Good night"
    my_dict = {"date_msg":date,"msg":msg}
    return render(request,"sunnyapp/home.html",context=my_dict)
def profiling(request):
    return render(request,"sunnyapp/profile.html")
