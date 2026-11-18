from django.urls import path
from . import views

app_name = 'contabilidad'

urlpatterns = [
    #agregar urls para contabilidad
    path('', views.dashboard, name='dashboard'),
    path('crear-cuenta/', views.crear_cuenta, name="crear_cuenta")
]
