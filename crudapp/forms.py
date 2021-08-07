from django import forms
from crudapp.models import EmployeeDetails

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=EmployeeDetails
        fields=('email','city')