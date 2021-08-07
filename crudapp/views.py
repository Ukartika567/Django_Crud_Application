from django.http import request, JsonResponse
from django.shortcuts import redirect, render
from .models import EmployeeDetails, Gender, City
from crudapp.forms import EmployeeForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json

# Function will show employees on table , Populate City & Gender,  pagination
def index(request):
    emp_list=EmployeeDetails.objects.all()
    genders=Gender.objects.all()
    cities=City.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(emp_list, 10)
    try:
        emps = paginator.page(page)
    except PageNotAnInteger:
        emps = paginator.page(1)
    except EmptyPage:
        emps = paginator.page(paginator.num_pages)
    return render(request, 'index.html', { 'emps': emps , 'emp_list': emp_list,'genders':genders, 'cities':cities})

# Insert data in DB by Ajax
def insert(request):
    name=request.POST['name']
    pannum=request.POST['pannum']
    age=request.POST['age']
    gender=request.POST['gender']
    city=request.POST['city']
    email=request.POST['email']    
    emp=EmployeeDetails(name=name, pannum=pannum, age=age, gender=gender, city=city, email=email)
    emp.save()
    return redirect('/')

# Validation if PAN Number existed or not  
def validate_PanNumber(request):
    PanNumber = request.GET.get('pannum', None)
    data = {
        'is_taken': EmployeeDetails.objects.filter(pannum=PanNumber).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'Employee with  this PAN Number already exists.'
    return JsonResponse(data)


# Function will edit/update the employee email and city  with the particular id
def edit_emp(request, id):
    emp_list=EmployeeDetails.objects.get(id=id)
    return render(request, 'index.html', {'emp_list':emp_list})

def emp_update(request, id):
    emps=EmployeeDetails.objects.get(id=id)
    form=EmployeeForm(request.POST, instance=emps)
    if form.is_valid:
        form.save()
        return redirect('/')
    return render(request, 'index.html', {'emps':emps})    


# Fuction will delete the particular employee with their id 
def delete_emp(request, id):
    emp=EmployeeDetails.objects.get(id=id)
    emp.delete()
    return redirect('/')