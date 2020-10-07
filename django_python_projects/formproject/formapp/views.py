from django.shortcuts import render
from . import forms
# Create your views here.

def thankyou(request):
    return render(request,"formapp/thankyou.html")

def studentregister(request):
    form = forms.StudentRegistration
    if request.method == 'POST':
        form = forms.StudentRegistration(request.POST)
        if form.is_valid():
            print("Form is validated")
            print("Student Name:",form.cleaned_data['name'])
            print("Student Rollno:",form.cleaned_data['rollno'])
            print("Student college:",form.cleaned_data['college'])
            print("Student password:",form.cleaned_data['password'])
            print("Student rpassword:",form.cleaned_data['rpassword'])
            print("Student Gpa:",form.cleaned_data['gpa'])
            print("Student Address:",form.cleaned_data['address'])
            return thankyou(request)


    return render(request,'formapp/register.html',{'form':form})
