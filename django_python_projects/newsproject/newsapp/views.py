from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"newsapp/index.html")
def sportsInfo(request):
    head_msg = "Latest information"
    msg1 = "Dhoni is in CSK"
    msg2 = "We had SRH vs RR"
    msg3 = "Today match is MI vs RCB"
    my_dict = {"head_msg":head_msg,"msg1": msg1,"msg2": msg2,"msg3": msg3}
    return render(request,"newsapp/news.html",context=my_dict)
def moviesInfo(request):
    head_msg = "Latest movies information"
    msg1 = "Bahubali is prabhas movie"
    msg2 = "Gharshana is venky movie"
    msg3 = "Bomarillu is family entertainer"
    my_dict = {"head_msg":head_msg,"msg1": msg1,"msg2": msg2,"msg3": msg3}
    return render(request,"newsapp/news.html",context=my_dict)
def politicsInfo(request):
    head_msg = "Latest politics information"
    msg1 = "Enadu"
    msg2 = "Andhrajyothi"
    msg3 = "Times of India"
    my_dict = {"head_msg":head_msg,"msg1": msg1,"msg2": msg2,"msg3": msg3}
    return render(request,"newsapp/news.html",context=my_dict)
