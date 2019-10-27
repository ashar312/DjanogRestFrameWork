from django import forms

from .models import employees

class Employeesform(forms.ModelForm):
    class Meta:
        model = employees
        fields = [
            'firstname',
            'lastname',
            'emp_id'
        ]