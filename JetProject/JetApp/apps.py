from django.apps import AppConfig


class JetappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'JetApp'

# from django.apps import AppConfig

class APP_NAMEConfig(AppConfig):
    name = 'APP_NAME'
    icon = 'ICON_CLASS'  # for example: icon = 'tim-icons icon-atom'