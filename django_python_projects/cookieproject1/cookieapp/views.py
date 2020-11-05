from django.shortcuts import render

# Create your views here.
def count_view(request):
    count = int(request.COOKIES.get("count",0))
    print(count)
    newcount = count + 1
    response = render(request,"cookieapp/count.html", {"count":newcount})
    response.set_cookie("count",newcount)
    return response
