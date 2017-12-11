from django import forms
from django.contrib.auth.models import User

class UserSignup(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password']

		widgets={
		'password': forms.PasswordInput(),
		}

class UserLogin(forms.Form):
	username = forms.Charfield(required=True)
	password = forms.Charfield(required=True, widget=forms.PasswordInput())