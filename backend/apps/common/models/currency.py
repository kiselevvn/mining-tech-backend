from django.db import models
from django.utils.translation import gettext as _


class CurrencyValues(models.Model):
    """
    Курс валют
    """

    # product = models.ForeignKey(
    #     "products.Product",
    #     verbose_name=_("Товар"),
    #     on_delete=models.CASCADE,
    #     related_name="pictures",
    # )
    # is_published = models.BooleanField(
    #     verbose_name=_("Изображение опубликовано"),
    #     default=False,
    #     blank=True,
    #     null=True,
    # )
    # order = models.PositiveIntegerField(verbose_name=_("Order"), default=0)
    # is_main = models.BooleanField(
    #     verbose_name=_("Товар в наличии"), default=False
    # )

    class Meta:
        verbose_name = _("Изображение товара")
        verbose_name_plural = _("Изображения товаров")

    def __str__(self):
        return self.product.name