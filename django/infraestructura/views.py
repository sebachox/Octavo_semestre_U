from django.shortcuts import render
from .models import NodoServidor


def lista_servidores(request):
    servidores = NodoServidor.objects.all()

    context = {
        'servidores': servidores
    }

    return render(request, 'infraestructura/index.html', context)