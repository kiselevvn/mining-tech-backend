from rest_framework.generics import CreateAPIView, ListAPIView

from backend.apps.orders.models import Order
from backend.apps.orders.serializers import OrderSerializer


class OrderListAPIView(ListAPIView):
    """
    """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class OrderCreateAPIView(CreateAPIView):
    """
    """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)