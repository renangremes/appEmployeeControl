from django.urls import path
from .views import index, company, employees, appointments

urlpatterns = [
    path('', index),
    path('company', company),
    path('employees', employees),
    path('appointments', appointments),
]