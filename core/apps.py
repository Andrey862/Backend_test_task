from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'core'

    def ready(self) -> None:
        from .service import bots
        from .models import TelegramData

        import os
        if os.environ.get('RUN_MAIN', None) != 'true':
            try:
                bots.up_bots(TelegramData.objects.filter(active=True))
            except Exception as e:
                print('faild CoreConfig.ready because', repr(e))
