from django import forms
from registration.models import Registration

class RegForm(forms.ModelForm):
	class Meta:
		model = Registration
		fiels = '__all__'
		exclude = ['created_date',]
		widgets = {
            'password': forms.PasswordInput(),
        }