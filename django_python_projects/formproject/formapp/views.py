from django.shortcuts import render
from . import forms
# Create your views here.
def studentregister(request):
    form = forms.StudentRegistration
    my_dict = {'form':form}
    return render(request,'formapp/register.html',context=my_dict)
