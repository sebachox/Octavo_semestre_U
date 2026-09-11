from rest_framework import serializers
from .models import NodoServidor, IncidenciaServidor, RegistroAuditoria


class NodoServidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = NodoServidor
        fields = "__all__"


class IncidenciaServidorSerializer(serializers.ModelSerializer):
    # Muestra el hostname en vez de solo el ID, sin perder el campo editable
    servidor_hostname = serializers.CharField(source="servidor.nombre_host", read_only=True)

    class Meta:
        model = IncidenciaServidor
        fields = "__all__"


class RegistroAuditoriaSerializer(serializers.ModelSerializer):
    servidor_hostname = serializers.CharField(source="servidor.nombre_host", read_only=True)

    class Meta:
        model = RegistroAuditoria
        fields = "__all__"