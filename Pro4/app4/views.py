from django.db import connection
from django.shortcuts import render,redirect
from django.views.generic.edit import FormView
from . forms import Category_Form, EmployeeForm, CategoryForm
from . models import Employee,Category


# Create your views here.

# def homepage(request):
#     return render(request,"app4/index.html")

def Employee_list(request):
    # context['workers'] = Worker.objects.all()
    # context={'Employee_list' = Employee.objects.all()}
    context={'Employee_list':Employee.objects.all()}
    return render(request,"app4/Employee_list.html",context)

def Employee_form(request,id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request,"app4/Employee_form.html",{'form':form})
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

def catagory_list(request):
    context={'Category_list':Category.objects.all()}
    return render(request,"app4/Category_list.html",context)

def catagory_form(request,id=0):
    if request.method == "GET":
        if id == 0:
            form = Category_Form()
        else:
            catagory = Category.objects.get(pk=id)
            form = Category_Form(instance=catagory)
        return render(request,"app4/Category_form.html",{'form':form})
    else:
        if id == 0:
            form = Category_Form(request.POST)
        else:
            catagory = Category.objects.get(pk=id)
            form = Category_Form(request.POST,instance=catagory)
            # form = EmployeeForm(request.POST, request.FILES, instance=form)
            # formset = BookInlineFormSet(request.POST, request.FILES, instance=author)
        if form.is_valid():
            form.save()
        return redirect('/categorylist')

def catagory_delete(request,id):
    catagory = Category.objects.get(pk=id)
    catagory.delete()
    return redirect('/categorylist')

def subcatagory(request):
    context={'subCategory_form':Category.objects.raw('SELECT * FROM app4_category WHERE "P_category_id" = 0')}
    # choice = forms.ModelChoiceField(queryset=MyChoices.objects.all())
    return render(request,'app4/Category_form.html',context)

# def sub_catagory(request):
#     category = Category.objects.all()
#     category_dict = {
#         'category': category
#     }
#     print(category.P_category_id)
#     # for c in category:    
#     #     print (c)
#     return render(request,'app4/subcatagory.html',category_dict)

# for p in Category.objects.raw('SELECT * FROM myapp_person'):
#     print(p)


# class CategoryFormView(FormView):
#     # specify the Form you want to use
#     form_class = CategoryForm
#     # specify name of template
#     template_name = "app4 / categorymodel_form.html"
#     # can specify success url
#     # url to redirect after successfully
#     # updating details
#     success_url ="/thanks/"