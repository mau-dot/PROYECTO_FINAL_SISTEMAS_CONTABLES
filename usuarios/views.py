from django.shortcuts import render, redirect
from .forms import RegistroForm, LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout

from django.http import HttpResponse
# Create your views here.


def login_view(request):
    if request.method == 'POST':
            form = LoginForm(request.POST, data=request.POST)
            if form.is_valid():
                usuario = form.get_user()
                login(request, usuario)
                return redirect('home')
            else:
                 print(form.errors)
                 messages.error(request, "Usuario o contraseña incorrectos")
    else:
         form = LoginForm()
    return render(request, 'usuarios/login.html', {'form': form})

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            return redirect('home')
    else:
         form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})


def logout_view(request):
     logout(request)
     return redirect('login')

@login_required
def perfil_view(request):
     return request(request, 'usuarios/perfil.html')


