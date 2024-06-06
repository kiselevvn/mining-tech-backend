from django.db import models
from django.utils.translation import gettext_lazy as _


class Address(models.Model):
    """
    Адрес
    """

    user = models.ForeignKey(
        "users.User",
        verbose_name=_("Пользователь"),
        on_delete=models.CASCADE,
        related_name="addresses"
    )
    value = models.TextField(_("Значение"))


    class Meta:
        verbose_name = _("Адрес")
        verbose_name_plural = _("Адреса")

