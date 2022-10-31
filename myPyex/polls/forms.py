#from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','password1','password2','email','codUs','sexUs','fechanacUs','telefonoUs','fotoUs','pagoUs','tarjetaUs','apuntados')