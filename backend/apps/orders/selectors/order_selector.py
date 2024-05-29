
from django.db.models import Prefetch

from backend.apps.common.services import BaseSelector
from backend.apps.orders.models import Order, OrderItem


class OrderItemSelector(BaseSelector):

    model = OrderItem

    @classmethod
    def get_list(cls):
        return cls.get_queryset().select_related("product").all()


class OrderSelector(BaseSelector):

    model = Order

    @classmethod
    def get_list(cls):
        p_items = Prefetch(
            lookup="items",
            queryset=OrderItemSelector.get_list()
        )
        return cls.get_queryset().prefetch_related(p_items).all()