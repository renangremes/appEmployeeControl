from django.contrib import admin
from .models import Appointments, Employees, Company

#Fields that will appear in the Admin
class AppointmentsAdmin(admin.ModelAdmin):
    list_display = ('PIS', 'date', 'hour')

class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('name', 'office', 'dateBirthday', 'PIS')

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'CNPJ')

admin.site.register(Appointments, AppointmentsAdmin)
admin.site.register(Employees, EmployeesAdmin)
admin.site.register(Company, CompanyAdmin)