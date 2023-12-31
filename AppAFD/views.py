import os
from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import Company, Employees, Appointments
from .convertAFD import convertAFD
from .forms import CompanyModelForm, EmployeesModelForm, AppointmentsModelForm

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


def appointments(request):

    lSucess = False
    months = [{'id':'01', 'month':'Jan'},
              {'id':'02', 'month':'Fev'},
              {'id':'03', 'month':'Mar'},
              {'id':'04', 'month':'Abr'},
              {'id':'05', 'month':'Mai'},
              {'id':'06', 'month':'Jun'},
              {'id':'07', 'month':'Jul'},
              {'id':'08', 'month':'Ago'},
              {'id':'09', 'month':'Set'},
              {'id':'10', 'month':'Out'},
              {'id':'11', 'month':'Nov'},
              {'id':'12', 'month':'Dez'}]

    years = ('2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029',
             '2030', '2031', '2032', '2033', '2034', '2035', '2036', '2037', '2038', '2039',
             '2040', '2041', '2042', '2043', '2044', '2045', '2046', '2047', '2048', '2049', '2050')

    if str(request.method) == 'POST' and request.FILES['file']:

        # Faz upload do arquivo para a pasta static/file
        file = request.FILES['file']
        storage = FileSystemStorage(location=settings.MEDIA_URL)
        filename = storage.save(file.name, file)
        uploaded_file_url = storage.url(filename)

        # Retorna lista com dados do arquivo importado
        arq = convertAFD(uploaded_file_url, "08382929000134")

        for line in arq:
            form = AppointmentsModelForm(line or None)

            # Valida se o formulário é válido
            if form.is_valid():
                # Valida se o PIS está cadastrado
                if Employees.objects.filter(PIS=line['PIS']).exists():
                    # Valida se já existe marcação com data/horário para o PIS
                    if Appointments.objects.filter(PIS=line['PIS'], date=line['date'], hour=line['hour']).exists():
                        form = AppointmentsModelForm()
                        #messages.error(request, "Já existente")
                    else:
                        form.save()  # Salva no banco
                        lSucess = True
                #else:
                #    messages.error(request, f"PIS {line['PIS']} não cadastrado na base")

            else:
                messages.error(request, "Erro ao importar")

        if lSucess:
            messages.success(request, "Arquivo importado com sucesso!")

    employees = Employees.objects.all()

    context = {
        "employees": employees,
        "months": months,
        "years": years
    }
    return render(request, 'appointments.html', context)