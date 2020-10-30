from django import forms
from registration.models import Registration

class RegForm(forms.ModelForm):
	class Meta:
		model = Registration
		exclude = ['created_date','last_login']
		widgets = {
            'password': forms.PasswordInput(),
        }
