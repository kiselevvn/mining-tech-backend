# from django.db import models
# from django.utils.translation import gettext as _


# class CurrencyValues(models.Model):
#     """
#     Курс валют
#     """


#     type = models.ForeignKey("common.CurrencyMining", verbose_name=_(""), on_delete=models.CASCADE)
#     class Meta:
#         verbose_name = _("Курс Валют")
#         verbose_name_plural = _("Курсы валют")

#     def __str__(self):
#         return self.product.name