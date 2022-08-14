from django.shortcuts import render, redirect

from home.models import department as department_model
from .models import employee as employee_model
# Create your views here.

def get_employees(request, id):
    employees_list = employee_model.objects.filter(department_id = id) ## return ve 1 list object
    department = department_model.objects.get(department_id = id) ## return ve 1 object
    
    return render(request, 'employees.html', {'employees_list': employees_list, 'department': department})

def get_employee_form(request):
    department_list = department_model.objects.filter()
    return render (request, 'employeesForm.html', {'department_list': department_list})

def add_employee(request):
    # print(request.method)
    if request.method == 'POST':
       department_id = request.POST['department']
       name = request.POST['fullname']
       age = request.POST['age']
       avatar = request.FILES['avatar']
       cv = request.FILES['cv']
       # do co khoa cua employee den department nen can phai lay doi tuong department de luu
       department = department_model.objects.get(department_id = department_id)
       
       employee = employee_model.objects.create(
           department_id = department,
           name = name,
           age = age,
           avatar = avatar,
           cv = cv,
       )
       
       print("employee: ", employee)
       
       employee.save()
       return redirect('/department/' + str(department_id))
    else:
        return render(request, 'error.html')