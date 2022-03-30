from django import forms
from .models import Employee,Category
# from crispy_bootstrap5.bootstrap5 import FloatingField

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = {  'Name',
                    'Surname',
                    'Gender',
                    'Department',
                    'City',
                    'position',
                    'Email',
                    'Display_picture',
                } 

    def __init__(self,*args,**kwargs):
        super(EmployeeForm,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label="select"

class Category_Form(forms.ModelForm):
    class Meta:
        model = Category
        fields = {  'category',
                    'sub_category',
                    
        }   


# # creating a form
# class CategoryForm(forms.Form):
#     # specify fields for model
#     title = forms.CharField()
#     description = forms.CharField(widget = forms.Textarea)