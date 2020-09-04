from django.urls import path
from .views import index, company, employees, appointments

urlpatterns = [
    path('', index, name='index'),
    path('company/', company, name='company'),
    path('employees/', employees, name='employees'),
    path('appointments/', appointments, name='appointments'),
]