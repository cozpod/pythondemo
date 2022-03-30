from cgitb import html
# from black import E
from django.shortcuts import render,redirect
# from matplotlib.style import context
from . forms import EmployeeForm
from . models import Employee
from django.forms.models import inlineformset_factory

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'JetApp/index.html')

# *********************************************************************************************************

def Category(request):
    # data='';
    # data['page']='category';
    # data['pageTitle']='Category';
    return render(request,'JetApp/category/index.html')

def Employee_list(request):
    # context['workers'] = Worker.objects.all()
    # context={'Employee_list' = Employee.objects.all()}
    context={'Employee_list':Employee.objects.all()}
    return render(request,"JetApp/Employee_list.html",context)


def Employee_form(request,id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request,"JetApp/Employee_form.html",{'form':form})
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

#############################################
# File Uploading
#############################################
# from .forms import EmployeeForm
# # from .models import User_Profile

# IMAGE_FILE_TYPE = ['jpg', 'png', 'jpeg']

# def Create_Profile(request):
#     form = EmployeeForm()
#     if request.method == 'POST':
#         form = EmployeeForm(request.POST, request.FILES)
#         if form.is_valid():
#             user_pr = form.save(commit=False)
#             user_pr.display_picture = request.FILES['Display_picture']
#             file_type = user_pr.display_picture.url.split('.')[-1]
#             file_type = file_type.lower()
#             if file_type not in IMAGE_FILE_TYPE:
#                 return render(request, 'error.html')
#             user_pr.save()
#             return render(request, 'details.html', {'user_pr': user_pr})
#     context = {'form': form, }
#     return render(request, 'create.html', context)

#############################################