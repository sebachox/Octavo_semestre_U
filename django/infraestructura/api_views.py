from rest_framework import viewsets
from .models import NodoServidor, IncidenciaServidor, RegistroAuditoria
from .serializers import (
    NodoServidorSerializer,
    IncidenciaServidorSerializer,
    RegistroAuditoriaSerializer,
)


class NodoServidorViewSet(viewsets.ModelViewSet):
    queryset = NodoServidor.objects.all()
    serializer_class = NodoServidorSerializer


class IncidenciaServidorViewSet(viewsets.ModelViewSet):
    queryset = IncidenciaServidor.objects.all()
    serializer_class = IncidenciaServidorSerializer


class RegistroAuditoriaViewSet(viewsets.ModelViewSet):
    queryset = RegistroAuditoria.objects.all()
    serializer_class = RegistroAuditoriaSerializer