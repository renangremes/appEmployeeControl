from django import forms
from .models import Appointments, Company, Employees

class ContactForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    subjects = forms.CharField(label='Assunto', max_length=8)
    message = forms.CharField(label='Mensagem', widget=forms.Textarea())

class EmployeesModelForm(forms.ModelForm):
    class Meta:
        model = Employees #Instancia qual model será usado para salvar em banco
        fields = [
            'name',
            'address',
            'postalCode',
            'city',
            'state',
            'office',
            'dateBirthday',
            'dateAdmission',
            'CPF',
            'RG',
            'PIS',
            'salary',
            'phone',
            'celPhone',
            'email'
        ]

class CompanyModelForm(forms.ModelForm):
    class Meta:
        model = Company #Instancia qual model será usado para salvar em banco
        fields = [
            'name',
            'CNPJ',
            'address',
            'postalCode',
            'city',
            'state',
            'phone',
            'celPhone',
            'email'
        ]

class AppointmentsModelForm(forms.ModelForm):
    class Meta:
        model = Appointments #Instancia qual model será usado para salvar em banco
        fields = [
            'date',
            'hour',
            'PIS'
        ]