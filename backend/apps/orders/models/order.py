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
        related_name="orders",
    )
    comment = models.TextField(
        verbose_name=_("Описание"), blank=True, null=True
    )
    invoice = models.JSONField(_("Счет"), default=dict())
    address = models.ForeignKey("users.Address", verbose_name=_("Адрес"), on_delete=models.PROTECT, blank=True, null=True)

    NEW = 1
    CREATED = 2
    CANCELED = 4
    PAID = 10

    STATUS = (
        (NEW, "Новый"),
        (CREATED, "Создан"),
        (PAID, "Оплачен"),
        (CANCELED, "Отменён"),
        # (ON_RECEIPT, "При получении"),
    )
    status = models.IntegerField(
        _("Статус заказа"),
        choices=STATUS,
        default=NEW,
    )
    date_created = models.DateTimeField(verbose_name=_("Дата создания"),auto_now_add=True)

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
