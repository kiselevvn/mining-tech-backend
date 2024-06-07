from rest_framework import serializers

from backend.apps.orders import models
from backend.apps.orders.services import OrderService


class OrderItemSerializer(serializers.ModelSerializer):
    """
    Картинка товара
    """

    product_id = serializers.CharField(source="product.id", required=False)
    product_name = serializers.CharField(source="product.name", required=False)
    category_name = serializers.CharField(source="product.category.name", required=False)


    class Meta:
        model = models.OrderItem
        fields = [
            "id",
            "product_id",
            "product_name",
            "category_name",
            "count",
        ]


class OrderSerializer(serializers.ModelSerializer):
    """
    Товар
    """

    items = OrderItemSerializer(many=True)
    price = serializers.SerializerMethodField()
    status_name = serializers.CharField(read_only=True, source="get_status_display")

    class Meta:
        model = models.Order
        fields = [
            "id",
            "status",
            "status_name",
            "date_created",
            "price",
            "items",
            "invoice",
            "address",
        ]

    def get_price(self, instance):
        return instance.price

    def create(self, validated_data):
        return OrderService.create(
            validated_data=validated_data,
            user=self.context.get("request").user
        )