from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext as _


class OrderItem(models.Model):
    """
    Позиция заказа
    """

    order = models.ForeignKey(
        "orders.Order",
        verbose_name=_("Заказ"),
        on_delete=models.CASCADE,
        related_name="items",
    )
    product = models.ForeignKey(
        "products.Product",
        verbose_name=_("Товар"),
        on_delete=models.CASCADE
    )
    count = models.IntegerField(_("Количество"))

    def __str__(self):
        return f"{self.product} (кол-во {self.count})"

    @property
    def price(self):
        """
        Сумма позиции
        """
        return self.count * self.product.price

    class Meta:
        verbose_name = _("Позиция заказа")
        verbose_name_plural = _("Позиции заказа")

