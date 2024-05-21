from django.db import transaction

from backend.apps.orders.models import Order, OrderItem


class OrderService():
    """
    """

    @classmethod
    def create(cls, validated_data, user):
        with transaction.atomic():
            order = Order(user=user)
            order.save()
            for item in validated_data.get("items"):
                order_item = OrderItem(
                    order=order,
                    product=item.get("product"),
                    count=item.get("count"),
                )
                order_item.save()

        return order


    # @classmethod
    # def cancel(cls, id_product):
    #     return True


    # @classmethod
    # def cancel(cls, id_product):
    #     return True