from django.urls import path
from .views import IndexView, company, employees, Appointments

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('company/', company, name='company'),
    path('employees/', employees, name='employees'),
    path('appointments/', Appointments, name='appointments'),
]