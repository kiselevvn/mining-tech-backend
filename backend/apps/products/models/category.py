from django.db import models
from django.utils.translation import gettext as _


class Category(models.Model):
    """
    Категория товара
    """

    name = models.CharField(verbose_name=_("Наименование"), max_length=255)
    is_published = models.BooleanField(
        verbose_name=_("Категория опубликована"), default=False
    )
    is_main = models.BooleanField(
        verbose_name=_("Является главной"), default=False
    )
    order = models.IntegerField(verbose_name=_("Order"), default=0)

    @property
    def count_products(self):
        return len(self.products.filter())

    class Meta:
        verbose_name = _("Категория товара")
        verbose_name_plural = _("Категории товара")
        ordering = ["is_main","order",]

    def __str__(self):
        return self.name