from django.shortcuts import render
from django.views import View


# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')

def descarga(request):
    return render(request, 'descarga/descargas.html')

