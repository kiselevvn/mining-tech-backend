from django.db import models
from django.utils.translation import gettext as _


class Picture(models.Model):
    """
    Изображение товара
    """

    product = models.ForeignKey(
        "products.Product",
        verbose_name=_("Товар"),
        on_delete=models.CASCADE,
        related_name="pictures",
    )
    image = models.ImageField(_("Изображение"), )

    is_published = models.BooleanField(
        verbose_name=_("Изображение опубликовано"),
        default=True,
    )
    order = models.PositiveIntegerField(verbose_name=_("Order"), default=0)
    is_main = models.BooleanField(
        verbose_name=_("Является главной"), default=False
    )

    class Meta:
        verbose_name = _("Изображение товара")
        verbose_name_plural = _("Изображения товаров")

    def __str__(self):
        return self.product.name