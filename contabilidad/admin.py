from django.contrib import admin
from .models import Cuenta, Partida, DetallePartida

# Register your models here.
admin.site.register([Cuenta, Partida, DetallePartida])

