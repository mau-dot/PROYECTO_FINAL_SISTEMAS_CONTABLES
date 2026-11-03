from django.urls import path
from . import views

urlpatterns = [
    #agregar urls para home
    path('', views.index, name='home'),
    
]