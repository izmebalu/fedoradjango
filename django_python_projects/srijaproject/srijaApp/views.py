from django.shortcuts import render
import datetime
from srijaApp.models import Employee
# Create your views here.
def timeinfo(request):
    date = datetime.datetime.now()
    my_dict = {'date_msg':date}
    return render(request,'srijaApp/wish.html',context = my_dict)
def flook(request):
    emp_list = Employee.objects.all()
    my_dict = {'emp_list':emp_list}
    return render(request,'srijaApp/hello.html',context=my_dict)
