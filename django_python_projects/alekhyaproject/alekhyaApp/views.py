from django.shortcuts import render
import datetime
# Create your views here.
def hasini(request):
    date = datetime.datetime.now()
    name = "Bunny"
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
    my_dict = {"date_msg":date,"guest":name,'msg':msg}
    return render(request,"alekhyaApp/hello.html",context=my_dict)
