from django.core import validators
from django import forms
from .models import User

class EmployeeRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
   