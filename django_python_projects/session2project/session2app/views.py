from django.shortcuts import render
from session2app.forms import NameForm,AgeForm,GfForm

# Create your views here.
def name_view(request):
    form = NameForm()
    return render (request,"session2app/name.html",{'form':form})

def age_view(request):
    name = request.GET['name']
    request.session['name']=name
    form = AgeForm()
    return render(request,"session2app/age.html",{'form':form})

def gf_view(request):
    age = request.GET['age']
    request.session['age']=age
    form = GfForm()
    return render(request,"session2app/gf.html",{'form':form})

def results_view(request):
    gf = request.GET['gf']
    request.session['gf']=gf
    return render(request,"session2app/results.html")
