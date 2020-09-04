# Generated by Django 3.1.1 on 2020-09-03 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='date')),
                ('hour', models.TimeField(verbose_name='hour')),
                ('PIS', models.CharField(max_length=12, verbose_name='PIS')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('CNPJ', models.CharField(max_length=14, verbose_name='CNPJ')),
                ('address', models.CharField(max_length=254, verbose_name='address')),
                ('postalCode', models.CharField(max_length=8, verbose_name='postalCode')),
                ('city', models.CharField(max_length=50, verbose_name='city')),
                ('state', models.CharField(max_length=2, verbose_name='state')),
                ('phone', models.CharField(max_length=10, verbose_name='phone')),
                ('celPhone', models.CharField(max_length=11, verbose_name='celPhone')),
                ('email', models.CharField(max_length=50, verbose_name='email')),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('address', models.CharField(max_length=254, verbose_name='address')),
                ('postalCode', models.CharField(max_length=8, verbose_name='postalCode')),
                ('city', models.CharField(max_length=50, verbose_name='city')),
                ('state', models.CharField(max_length=2, verbose_name='state')),
                ('office', models.CharField(max_length=50, verbose_name='office')),
                ('dateBirthday', models.DateField(verbose_name='dateBirthday')),
                ('dateAdmission', models.DateField(verbose_name='dateAdmission')),
                ('CPF', models.CharField(max_length=11, verbose_name='CPF')),
                ('RG', models.CharField(max_length=9, verbose_name='RG')),
                ('PIS', models.CharField(max_length=12, verbose_name='PIS')),
                ('salary', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='salary')),
                ('phone', models.CharField(max_length=10, verbose_name='phone')),
                ('celPhone', models.CharField(max_length=11, verbose_name='celPhone')),
                ('email', models.CharField(max_length=50, verbose_name='email')),
            ],
        ),
    ]
