from django.apps import AppConfig


class CommonConfig(AppConfig):
    """
    Осмотр спортсменов
    """

    default_auto_field = "django.db.models.AutoField"
    name = "backend.apps.common"
    verbose_name = "4. Справочники"
