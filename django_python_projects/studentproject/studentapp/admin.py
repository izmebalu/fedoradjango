from django.contrib import admin
from studentapp.models import Student
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','marks']
# Register your models here.
admin.site.register(Student,StudentAdmin)
