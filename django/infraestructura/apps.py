from django.apps import AppConfig


class InfraestructuraConfig(AppConfig):
    name = 'infraestructura'

    def ready(self):
            import infraestructura.signals  # noqa