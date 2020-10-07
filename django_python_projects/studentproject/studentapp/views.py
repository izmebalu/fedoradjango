from django.shortcuts import render
from studentapp import forms
from studentapp.models import Student
# Create your views here.
def student_view(request):
    form = forms.StudentForm()
    if request.method == 'POST':
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print("Inserted into the database successfully")
    return render(request,"studentapp/register.html",{'form':form})

def list_view(request):
    stud_list = Student.objects.all()
    return render(request,'studentapp/list_student.html',{"stud_list":stud_list})
