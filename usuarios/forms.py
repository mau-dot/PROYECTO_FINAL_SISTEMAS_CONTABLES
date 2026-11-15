from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from .models import Usuario
from django.contrib.auth import get_user_model


User = get_user_model()

class RegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username' ,'email', 'password1', 'password2']
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Atrapamos el error antes de que llegue a la base de datos
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está registrado en el sistema.")
        return email


class LoginForm(AuthenticationForm):
    pass


class CustomPasswordResetForm(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Verificamos si el correo existe en la base de datos
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("No existe ninguna cuenta asociada a este correo.")
        return email