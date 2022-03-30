from django import forms
from .models import Employee

class Upload_Profile(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['fname','lname','technologies','email','display_picture']
