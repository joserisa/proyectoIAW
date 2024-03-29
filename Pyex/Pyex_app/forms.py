#from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','password1','password2','email')


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class Ocupacion(forms.Form):

	ocupar = forms.BooleanField(required=False)

class Desocupacion(forms.Form):

	desocupar = forms.BooleanField(required=False)
