from django.contrib import admin

from backend.apps.products import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

class PictureInlineAdmin(admin.TabularInline):
    model = models.Picture
    extra = 0

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [PictureInlineAdmin,]
    search_fields = ["name", "pk"]
    list_filter = [
        "category",
        "is_published",
        "is_available",
        "is_pre_order",
    ]
    list_display = [
        "name",
        "price",
        "category",
        "is_published",
        "is_available",
        "is_pre_order",
        "date_updated",
        "date_created",
    ]
    list_editable = [
        "category",
        "price",
        "is_published",
        "is_available",
        "is_pre_order",
    ]
