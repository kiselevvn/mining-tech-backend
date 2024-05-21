from django.db import models
from django.utils.translation import gettext as _


class Brand(models.Model):
    """
    """

    name = models.CharField(_("Наименование"), max_length=200)

    class Meta:
        verbose_name = _("Производитель")
        verbose_name_plural = _("Производители")

    def __str__(self):
        return self.name


class Algorithm(models.Model):
    """
    """

    name = models.CharField(_("Наименование"), max_length=50)

    class Meta:
        verbose_name = _("Алгоритм шифрования")
        verbose_name_plural = _("Алгоритмы шифрования")

    def __str__(self):
        return self.name


class CurrencyMining(models.Model):
    """
    """

    name = models.CharField(_("Наименование"), max_length=50)

    class Meta:
        verbose_name = _("Валюта")
        verbose_name_plural = _("Валюты")

    def __str__(self):
        return self.name


class Hashrate(models.Model):
    """
    """

    TYPES = (
        ("TH/S", "TH/S"),
        ("МH/S", "МH/S"),
        ("GH/S", "GH/S"),
        ("K/SOL", "K/SOL"),
    )
    value = models.IntegerField(_("Значение"))
    type = models.CharField(_("Еденица измерения"), choices=TYPES, max_length=50)

    class Meta:
        verbose_name = _("Хешрейт")
        verbose_name_plural = _("Хешрейт")

    def __str__(self):
        return f"{str(self.value)} {self.type}"


class Power(models.Model):
    """
    """

    value = models.IntegerField(_("Значение"))

    class Meta:
        verbose_name = _("Потребление энергии")
        verbose_name_plural = _("Потребление энергии")

    def __str__(self):
        return f"{str(self.value)} W"