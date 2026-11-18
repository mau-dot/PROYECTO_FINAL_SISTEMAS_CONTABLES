from django import forms
from .models import Cuenta

class CuentaForm(forms.ModelForm):
    class Meta:
        model = Cuenta
        # campos exactos que tienes en tu modelo Cuenta
        #'codigo', 'nombre', 'tipo_cuenta'
        fields = ['codigo', 'nombre', 'tipo']
        
        # Opcional: Personalizamos las etiquetas para que se vean mejor en pantalla
        labels = {
            'codigo': 'Código de la Cuenta',
            'nombre': 'Nombre de la Cuenta',
            'tipo': 'Clasificación (Activo, Pasivo, etc.)'
        }


