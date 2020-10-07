from django.shortcuts import render
from testapp.models import Employee
emp_list = Employee.objects.all()
# Create your views here.
def indexing(request):
    return render(request,"testapp/index.html")
def data(request):
    my_dict = {'emp_list':emp_list}
    return render(request,"testapp/hello.html",context=my_dict)
