from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib import messages
from .models import Company, Employees, Appointments
from .convertAFD import convertAFD
from .forms import CompanyModelForm, EmployeesModelForm
from datetime import datetime

#Here you define the views. Receive parameter "request" and return a render (html page)
#To access the views below, you need to create the route in the urls.py file in project

class IndexView(TemplateView):
    template_name = 'index.html'


def employees(request):
    form = EmployeesModelForm(request.POST or None) #Parâmetros, pode conter dados ou não. Exemplo: request.POST (tem dados) / None (vazio)

    if str(request.method) == 'POST': #Se for POST
        form = EmployeesModelForm(request.POST)
        if form.is_valid(): #Valida se o formulário é válido

            # Exemplo pegar dados do request
            CPF = form.cleaned_data['CPF']
            PIS = form.cleaned_data['PIS']

            if Employees.objects.filter(CPF=CPF).exists():
                messages.error(request, 'CPF já cadastrado')
            elif Employees.objects.filter(PIS=PIS).exists():
                messages.error(request, 'PIS já cadastrado')
            else:
                form.save() #Salva no banco

                messages.success(request, 'Cadastrado com sucesso!')
                form = EmployeesModelForm() #Limpa formulário
        else:
            messages.error(request, 'Erro ao cadastrar')
    else:
        form = EmployeesModelForm()  # Limpa formulário

    context = {
        'form': form
    }
    return render(request, 'employees.html', context)


def company(request):
    form = CompanyModelForm(request.POST or None) #Parâmetros, pode conter dados ou não. Exemplo: request.POST (tem dados) / None (vazio)

    if str(request.method) == 'POST': #Se for POST
        form = CompanyModelForm(request.POST)
        if form.is_valid(): #Valida se o formulário é válido

            # Exemplo pegar dados do request
            CNPJ = form.cleaned_data['CNPJ']

            if Company.objects.filter(CNPJ=CNPJ).exists():
                messages.error(request, 'CNPJ já cadastrado')
            else:
                form.save() #Salva no banco

                messages.success(request, 'Cadastrado com sucesso!')
                form = CompanyModelForm() #Limpa formulário
        else:
            messages.error(request, 'Erro ao cadastrar')
    else:
        form = CompanyModelForm()  # Limpa formulário

    context = {
        'form': form
    }
    return render(request, 'company.html', context)


class AppointmentsView(TemplateView):
    template_name = 'appointments.html'

    def get_context_data(self, **kwargs):
        context = super(AppointmentsView, self).get_context_data(**kwargs) #Recuperando contexto
        context['list_appointments'] = convertAFD('C:/Temp/AFD.txt', '08382929000134') #Adicionando dados ao contexto
        return context