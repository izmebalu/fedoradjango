from django.shortcuts import render

# Create your views here.
def name_view(request):
    return render(request,"cookiesapp/name.html")

def age_view(request):
    name = request.GET['name']
    response = render(request,"cookiesapp/age.html")
    response.set_cookie('name',name)
    return response

def gf_view(request):
    age = request.GET['age']
    response = render(request,"cookiesapp/gf.html")
    response.set_cookie('age',age)
    return response

def results_view(request):
    gf = request.GET['gf']
    age = request.COOKIES.get('age')
    name = request.COOKIES.get('name')
    response =  render(request,"cookiesapp/results.html",{'name':name,'age':age,'gf':gf})
    return response
