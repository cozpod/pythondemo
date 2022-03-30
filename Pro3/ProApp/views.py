from django.shortcuts import render
from django.shortcuts import render,redirect
from . forms import EmployeeForm
from . models import Employee

# Create your views here.

def index(request):
    return render(request,('ProApp/index.html'))

def Employee_list(request):
    # context['workers'] = Worker.objects.all()
    # context={'Employee_list' = Employee.objects.all()}
    context={'Employee_list':Employee.objects.all()}
    return render(request,"ProApp/Employee_list.html",context)

def Employee_form(request,id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request,"ProApp/Employee_form.html",{'form':form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance=employee)
            # form = EmployeeForm(request.POST, request.FILES, instance=form)
            # formset = BookInlineFormSet(request.POST, request.FILES, instance=author)
        if form.is_valid():
            form.save()
        return redirect('/list')
    

def Employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/list')
