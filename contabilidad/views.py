from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CuentaForm
from .models import Cuenta
# Create your views here.


@login_required
def crear_cuenta(request):
    if request.method == "POST":
        form = CuentaForm(request.POST)
        if form.is_valid():
            form.save()
            #mensaje de exito
            messages.success(request,"La cuenta contable se creo correctamente")
            #rendirigimos al catalogo   
            return redirect('contabilidad:crear_cuenta')
    else:
        form = CuentaForm()

    #traer las cuentas existentes para mostrar
    cuentas_existentes = Cuenta.objects.all().order_by('codigo')

    contexto = {
        'form' : form,
        'cuentas' : cuentas_existentes  
    }

    return render(request, 'contabilidad/crear_cuenta.html', contexto)


@login_required
def dashboard(request):
    return render(request, 'contabilidad/dashboard.html')