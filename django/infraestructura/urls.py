from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_servidores, name='lista_servidores'),
    path('servidor/<int:pk>/', views.detalle_servidor, name='detalle_servidor'),
    path('servidor/nuevo/', views.crear_servidor, name='crear_servidor'),
    path('servidor/<int:pk>/editar/', views.editar_servidor, name='editar_servidor'),
    path('servidor/<int:pk>/eliminar/', views.eliminar_servidor, name='eliminar_servidor'),
    path("servidor/<int:servidor_pk>/incidencia/nueva/", views.crear_incidencia, name="crear_incidencia"),
    path("incidencia/<int:pk>/resolver/", views.resolver_incidencia, name="resolver_incidencia"),
]