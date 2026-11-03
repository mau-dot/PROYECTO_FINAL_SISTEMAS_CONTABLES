from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def login_view(request):
    return HttpResponse("PAGINA DE LOGIN")

def registro_view(request):
    return HttpResponse("PAGINA DE REGISTRO")


