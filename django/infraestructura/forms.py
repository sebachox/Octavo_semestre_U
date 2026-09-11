from django import forms
from .models import NodoServidor, IncidenciaServidor

class NodoServidorForm(forms.ModelForm):
    class Meta:
        model = NodoServidor
        fields = ['nombre_host', 'direccion_ip', 'motor_contenedores', 'proxy_inverso', 'en_produccion']


class IncidenciaServidorForm(forms.ModelForm):

    class Meta:
        model = IncidenciaServidor
        fields = ["servidor", "titulo", "descripcion", "severidad"]
        widgets = {
            "servidor": forms.Select(attrs={"class": "form-select"}),
            "titulo": forms.TextInput(attrs={
                "class": "form-control ",
                "placeholder": "Título breve de la incidencia"
            }),
            "descripcion": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Describe el fallo o evento crítico"
            }),
            "severidad": forms.Select(attrs={"class": "form-select"}),
        }