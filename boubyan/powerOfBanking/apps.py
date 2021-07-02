from django.apps import AppConfig


class PowerofbankingConfig(AppConfig):
    name = 'powerOfBanking'

    def ready(self):
        from . import signals
