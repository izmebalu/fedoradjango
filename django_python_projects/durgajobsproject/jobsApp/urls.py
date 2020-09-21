from django.urls import path
from jobsApp import views

urlpatterns = [
    path('mumbai/', views.mumbai),
    path('pune/', views.pune),
    path('hyd/', views.hyd),

]
