from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_servidores, name='lista_servidores'),
    path('servidor/<int:pk>/', views.detalle_servidor, name='detalle_servidor'),
]