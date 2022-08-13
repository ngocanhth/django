from django.shortcuts import render

from home.models import department as department_model
from .models import employee as employee_model
# Create your views here.

def get_employees(request, id):
    employees_list = employee_model.objects.filter(department_id = id) ## return ve 1 list object
    department = department_model.objects.get(department_id = id) ## return ve 1 object
    
    return render(request, 'employees.html', {'employees_list': employees_list, 'department': department})