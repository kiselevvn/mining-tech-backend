from django.contrib import admin

from backend.apps.common import models


@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Algorithm)
class AlgorithmAdmin(admin.ModelAdmin):
    pass

@admin.register(models.CurrencyMining)
class CurrencyMiningAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Hashrate)
class HashrateAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Power)
class PowerAdmin(admin.ModelAdmin):
    pass