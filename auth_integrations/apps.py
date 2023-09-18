from django.apps import AppConfig


class AuthIntegrationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auth_integrations'

    def ready(self):
        from .signals import register_signals

        register_signals()
