from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#vista de pagina principal index
def index(request):
    #render toma el request y el archivo html que se espera mostrar 
    return render(request, "home/index.html")

