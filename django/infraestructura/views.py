from django.shortcuts import render, get_object_or_404
from .models import NodoServidor


def detalle_servidor(request, pk):
    nodo = get_object_or_404(NodoServidor, pk=pk)
    return render(request, 'infraestructura/detalle.html', {'nodo': nodo})

def lista_servidores(request):

    servidores = NodoServidor.objects.all()
    context = {'servidores': servidores}
    return render(request, 'infraestructura/index.html', context)