from django.db import models
from django.utils.translation import gettext as _


class Product(models.Model):
    """
    Товар
    """

    name = models.CharField(verbose_name=_("Наименование"), max_length=500)
    price = models.DecimalField(
        verbose_name=_("Цена"),
        max_digits=10,
        decimal_places=2,
    )
    short_description = models.TextField(
        verbose_name=_("Краткое описание"), blank=True, null=True
    )
    description = models.TextField(
        verbose_name=_("Описание"), blank=True, null=True
    )
    category = models.ForeignKey(
        "products.Category",
        verbose_name=_("Категория"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="products",
    )
    brand = models.ForeignKey(
        "common.Brand",
        verbose_name=_("Производитель"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    algorithm = models.ForeignKey(
        "common.Algorithm",
        verbose_name=_("Алгоритм шифрования"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    currency_mining = models.ForeignKey(
        "common.CurrencyMining",
        verbose_name=_("Валюта"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    hashrate = models.ForeignKey(
        "common.Hashrate",
        verbose_name=_("Хешрейт"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    power = models.ForeignKey(
        "common.Power",
        verbose_name=_("Потребление энергии"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    is_published = models.BooleanField(
        verbose_name=_("Товар опубликован"), default=False
    )
    is_available = models.BooleanField(
        verbose_name=_("Товар в наличии"), default=False
    )
    is_pre_order = models.BooleanField(
        verbose_name=_("Доступен предзаказ"), default=False
    )
    count = models.IntegerField(_("Количство товара"), default=0)

    date_updated = models.DateTimeField(auto_now=True)

    date_created = models.DateTimeField(auto_now_add=True)

    def main_image(self):
        return self.pictures.filter(
            is_main=True, is_published=True
        ).first()


    objects = models.Manager()
    class Meta:
        verbose_name = _("Товар")
        verbose_name_plural = _("Товары")
    def __str__(self):
        return self.name
