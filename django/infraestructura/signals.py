from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import NodoServidor, RegistroAuditoria


@receiver(post_save, sender=NodoServidor)
def registrar_creacion_nodo(sender, instance, created, **kwargs):
    """
    Se ejecuta automáticamente cada vez que se guarda un NodoServidor.
    'created' es True solo la primera vez (cuando se INSERTA, no cuando se actualiza).
    """
    if created:
        RegistroAuditoria.objects.create(
            servidor=instance,
            detalles=f"Nodo '{instance.nombre_host}' ({instance.direccion_ip}) fue creado."
        )


@receiver(pre_delete, sender=NodoServidor)
def registrar_eliminacion_nodo(sender, instance, **kwargs):
    """
    Se ejecuta justo ANTES de que el nodo sea eliminado (pre_delete, no post_delete),
    porque una vez eliminado ya no podríamos crear un registro con FK hacia él.
    """
    RegistroAuditoria.objects.create(
        servidor=instance,
        detalles=f"Nodo '{instance.nombre_host}' ({instance.direccion_ip}) fue eliminado."
    )