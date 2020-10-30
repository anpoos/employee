from django import forms
from django.forms.widgets import DateInput
from emp.models import Employee

class EmpForm(forms.ModelForm):
	class Meta:
		model = Employee
		fiels = '__all__'
		exclude = ['is_active','is_deleted','created_date','updated_date']
		widgets = {
            'dob': DateInput(attrs={'type': 'date'}),
        }