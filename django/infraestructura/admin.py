from django.contrib import admin
from .models import NodoServidor, RegistroAuditoria


@admin.register(NodoServidor)
class NodoServidorAdmin(admin.ModelAdmin):

    list_display = (
        "nombre_host",
        "direccion_ip",
        "motor_contenedores",
        "proxy_inverso",
        "en_produccion",
    )

    list_filter = (
        "motor_contenedores",
        "proxy_inverso",
        "en_produccion",
    )

    search_fields = (
        "nombre_host",
        "direccion_ip",
    )

    ordering = (
        "-fecha_despliegue",
    )

    actions = [
        "marcar_como_produccion",
        "marcar_como_mantenimiento",
    ]

    @admin.action(description="Activar Producción Masiva")
    def marcar_como_produccion(self, request, queryset):
        actualizados = queryset.update(en_produccion=True)
        for nodo in queryset:
            RegistroAuditoria.objects.create(
                servidor=nodo,
                detalles=f"Nodo puesto en producción por {request.user}."
            )
        self.message_user(
            request,
            f"{actualizados} nodo(s) marcado(s) como en producción."
        )

    @admin.action(description="Poner en Mantenimiento")
    def marcar_como_mantenimiento(self, request, queryset):
        actualizados = queryset.update(en_produccion=False)
        for nodo in queryset:
            RegistroAuditoria.objects.create(
                servidor=nodo,
                detalles=f"Nodo puesto en mantenimiento por {request.user}."
            )
        self.message_user(
            request,
            f"{actualizados} nodo(s) puesto(s) en mantenimiento."
        )


@admin.register(RegistroAuditoria)
class RegistroAuditoriaAdmin(admin.ModelAdmin):
    list_display = ("servidor", "detalles", "fecha_evento")
    list_filter = ("servidor",)
    ordering = ("-fecha_evento",)