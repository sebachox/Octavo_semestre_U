from django.shortcuts import render, get_object_or_404, redirect
from .models import NodoServidor, IncidenciaServidor
from .forms import NodoServidorForm, IncidenciaServidorForm

def eliminar_servidor(request, pk):
    nodo = get_object_or_404(NodoServidor, pk=pk)
    if request.method == 'POST':
        nodo.delete()
        return redirect('home_servidores')
    return render(request, 'infraestructura/eliminar_servidor.html', {'nodo': nodo})


def editar_servidor(request, pk):
    nodo = get_object_or_404(NodoServidor, pk=pk)
    if request.method == 'POST':
        form = NodoServidorForm(request.POST, instance=nodo)
        if form.is_valid():
            form.save()
            return redirect('detalle_servidor', pk=nodo.pk)
    else:
        form = NodoServidorForm(instance=nodo)
    return render(request, 'infraestructura/editar_servidor.html', {'form': form, 'nodo': nodo})


def crear_servidor(request):
    if request.method == 'POST':
        form = NodoServidorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_servidores')
    else:
        form = NodoServidorForm()
    return render(request, 'infraestructura/crear_servidor.html', {'form': form})


def detalle_servidor(request, pk):
    nodo = get_object_or_404(NodoServidor, pk=pk)
    incidencias = nodo.incidencias.all()
    return render(request, "infraestructura/detalle.html", {
        "nodo": nodo,
        "incidencias": incidencias,
    })


def crear_incidencia(request, servidor_pk):
    servidor = get_object_or_404(NodoServidor, pk=servidor_pk)

    if request.method == "POST":
        form = IncidenciaServidorForm(request.POST, initial={"servidor": servidor})
        if form.is_valid():
            form.save()
            return redirect("detalle_servidor", pk=servidor.pk)
    else:
        form = IncidenciaServidorForm(initial={"servidor": servidor})

    return render(request, "infraestructura/incidencia_form.html", {
        "form": form,
        "servidor": servidor,
    })


def resolver_incidencia(request, pk):
    incidencia = get_object_or_404(IncidenciaServidor, pk=pk)
    incidencia.resuelta = True
    incidencia.save()
    return redirect("detalle_servidor", pk=incidencia.servidor.pk)

def lista_servidores(request):

    servidores = NodoServidor.objects.all()
    context = {'servidores': servidores}
    return render(request, 'infraestructura/index.html', context)