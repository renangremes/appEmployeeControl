from django.db import models

#Models of database
class Appointments(models.Model):
    date = models.DateField('date')
    hour = models.TimeField('hour')
    PIS = models.CharField('PIS', max_length=12)

    #Methodo __str__ return description model
    def __str__(self):
        return self.PIS

class Employees(models.Model):
    name = models.CharField('name', max_length=100)
    address = models.CharField('address', max_length=254)
    postalCode = models.CharField('postalCode', max_length=8)
    city = models.CharField('city', max_length=50)
    state = models.CharField('state', max_length=2)
    office = models.CharField('office', max_length=50)
    dateBirthday = models.DateField('dateBirthday')
    dateAdmission = models.DateField('dateAdmission')
    CPF = models.CharField('CPF', max_length=11)
    RG = models.CharField('RG', max_length=9)
    PIS = models.CharField('PIS', max_length=12)
    salary = models.DecimalField('salary', decimal_places=2, max_digits=8)
    phone = models.CharField('phone', max_length=10)
    celPhone = models.CharField('celPhone', max_length=11)
    email = models.CharField('email', max_length=50)

    #Methodo __str__ return description model
    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField('name', max_length=100)
    CNPJ = models.CharField('CNPJ', max_length=14)
    address = models.CharField('address', max_length=254)
    postalCode = models.CharField('postalCode', max_length=8)
    city = models.CharField('city', max_length=50)
    state = models.CharField('state', max_length=2)
    phone = models.CharField('phone', max_length=10)
    celPhone = models.CharField('celPhone', max_length=11)
    email = models.CharField('email', max_length=50)

    #Methodo __str__ return description model
    def __str__(self):
        return self.name
