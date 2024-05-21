from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext as _


class CartItem(models.Model):
    """
    Позиция заказа
    """

    user = models.ForeignKey(
        "users.User",
        verbose_name=_("Пользователь"),
        on_delete=models.CASCADE,
        related_name="cart_items",
    )
    product = models.ForeignKey(
        "products.Product",
        verbose_name=_("Товар"),
        on_delete=models.CASCADE
    )
    count = models.IntegerField(_("Количество"))

    def __str__(self):
        return f"{self.product} (кол-во {self.count})"

    class Meta:
        verbose_name = _("Позиция заказа")
        verbose_name_plural = _("Позиции заказа")
