from django.contrib import admin
from .models import Appointments, Employees, Company

#Fields that will appear in the Admin
@admin.register(Appointments)
class AppointmentsAdmin(admin.ModelAdmin):
    list_display = ('PIS', 'date', 'hour')

@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('name', 'office', 'dateBirthday', 'PIS')

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'CNPJ')