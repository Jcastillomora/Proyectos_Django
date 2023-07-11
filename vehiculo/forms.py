from django import forms
from .models import Vehiculo

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class VehiculoForm(forms.ModelForm):

    class Meta:
        model = Vehiculo
        fields = '__all__'

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        #fields = ['username', 'email', 'password1', 'password2']
        fields = ('username', 'email', 'password1', 'password2')
