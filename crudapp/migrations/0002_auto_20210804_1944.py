# Generated by Django 3.2.6 on 2021-08-05 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeedetails',
            name='age',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='employeedetails',
            name='city',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='employeedetails',
            name='gender',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='employeedetails',
            name='pannum',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='employeedetails',
            name='email',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='employeedetails',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]