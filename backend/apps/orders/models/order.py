from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils.translation import gettext as _


class Order(models.Model):
    """
    Заказ
    """

    user = models.ForeignKey(
        "users.User",
        verbose_name=_("Пользователь"),
        on_delete=models.CASCADE,
        related_name="cart",
    )
    comment = models.TextField(
        verbose_name=_("Описание"), blank=True, null=True
    )

    NEW = 1
    PAID = 2
    CANCELED = 3
    # ON_RECEIPT = 4
    # CLOSE = 5

    STATUS = (
        (NEW, "Новый"),
        (PAID, "Оплачен"),
        (CANCELED, "Отменён"),
        # (ON_RECEIPT, "При получении"),
        # (CLOSE, "Закрыт"),
    )
    status = models.IntegerField(
        _("Статус заказа"),
        choices=STATUS,
        default=NEW,
    )
    date_created = models.DateTimeField(auto_now_add=True)

    @property
    def price(self):
        """
        Сумма заказа
        """
        price = 0
        for i in self.items.all():
            price += i.price
        return price

    class Meta:
        verbose_name = _("Заказ")
        verbose_name_plural = _("Заказы")
        ordering = ["-date_created"]

    def __str__(self):
        return f"{self.user.username} {self.price}"
