from django.db import models

# Create your models here.
class EmployeeDetails(models.Model):
    name=models.CharField(max_length=100)
    pannum=models.CharField(max_length=100, default='')
    age=models.CharField(max_length=100, default='')
    gender=models.CharField(max_length=50, default='')
    city=models.CharField(max_length=100, default='')
    email=models.CharField(max_length=100, default='')

    class Meta:
        db_table='employeedetails'

class Gender(models.Model):
    gender=models.CharField(max_length=100)

    class Meta:
        db_table='gendertable'

class City(models.Model):
    City=models.CharField(max_length=100)

    class Meta:
        db_table='citytable'                    