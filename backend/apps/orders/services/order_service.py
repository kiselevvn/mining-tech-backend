from django.conf import settings
from django.db import transaction

from backend.apps.common.services import CryptoCloudSDK
from backend.apps.orders.models import Order, OrderItem


class OrderService():
    """
    """

    cc_sdk = CryptoCloudSDK(api_key=settings.CRYPTO_CLOUD_API_KEY)

    @classmethod
    def create(cls, validated_data, user):
        instance = cls.create_instance(validated_data, user)
        return instance

    @classmethod
    def check_status_orders(cls, orders):
        for o in orders:
            cls.check_status_order(o)

    @classmethod
    def check_status_order(cls, order):
        if order.status == order.NEW:
            cls._create_invoice_order(order)
        if order.status == order.CREATED:
            cls._check_status_invoice_order(order)
        else:
            pass


    @classmethod
    def _check_status_invoice_order(cls, order):
        status  = cls.cc_sdk.get_invoice_info(
            uuids = [order.invoice["result"]["uuid"],]
        )
        invoice_status = status["result"][0]["invoice_status"]
        if invoice_status == 'success':
            order.status = order.PAID
            order.save()
        elif invoice_status == 'canceled':
            order.status = order.CANCELED
            order.save()
        # print(str(status["invoice_status"], status["date_finished"]))
        # if status.result.date_finished != None:

    @classmethod
    def _create_invoice_order(cls, order):
        data = {
            "shop_id": settings.CRYPTO_CLOUD_SHOP_ID,
            "currency": "RUB",
            "amount": order.price,
            "order_id": order.pk,
        }
        invoice  = cls.cc_sdk.create_invoice(
            invoice_data = data
        )
        order.invoice = invoice
        order.status = order.CREATED
        order.save()

    @classmethod
    def create_instance(cls, validated_data, user):
        with transaction.atomic():
            order = Order(user=user)
            order.save()
            for item in validated_data.get("items"):
                # print(item)
                order_item = OrderItem(
                    order=order,
                    product_id=item.get("product")["id"],
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