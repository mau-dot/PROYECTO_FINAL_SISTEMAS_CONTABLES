from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario

class RegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'nombres', 'apellidos', 'edad', 'email', 'password1', 'password2', ]


class LoginForm(AuthenticationForm):
    pass