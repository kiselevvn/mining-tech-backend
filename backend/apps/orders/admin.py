from django.contrib import admin

from backend.apps.orders import models


class OrderItemInlineAdmin(admin.StackedInline):
    model = models.OrderItem
    extra = 0


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):

    inlines = [OrderItemInlineAdmin,]

    search_fields = ["user",]

    list_filter = [
        "status",
    ]
    list_display = [
        "date_created",
        "user",
        "status",
    ]
    # list_editable = [
    #     "status",
    # ]
