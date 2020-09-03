from django.shortcuts import render
from .models import Company, Employees, Appointments
from .convertAFD import convertAFD

#Here you define the views. Receive parameter "request" and return a render (html page)
#To access the views below, you need to create the route in the urls.py file in project

def index(request):
    company = Company.objects.filter(CNPJ='14413700000112')
    print(company.values('CNPJ'))
    list_appointments = convertAFD('C:/Temp/AFD.txt', '14413700000112')

    context = {
        'list_appointments': list_appointments,
    }

    return render(request, 'index.html', context)

def employees(request):
    return render(request, 'employees.html')

def company(request):
    return render(request, 'company.html')

def appointments(request):
    return render(request, 'appointments.html')