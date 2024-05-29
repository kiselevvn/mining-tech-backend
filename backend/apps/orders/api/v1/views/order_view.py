from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from backend.apps.orders.models import Order
from backend.apps.orders.selectors import OrderSelector
from backend.apps.orders.serializers import OrderSerializer
from backend.apps.orders.services import OrderService


class PostbackView(APIView):

    def post(self, request):
        status = request.data.get('status')
        invoice_id = request.data.get('invoice_id')
        amount_crypto = request.data.get('amount_crypto')
        currency = request.data.get('currency')
        order_id = request.data.get('order_id')
        token = request.data.get('token')
        o = Order.objects.get(pk=int(order_id))
        o.status = o.PAID
        o.save()
        return Response({'message': 'Postback received'})


class OrderListAPIView(ListAPIView):
    """
    """

    authentication_classes = [JWTAuthentication,]
    serializer_class = OrderSerializer

    def get_queryset(self):
        qs = OrderSelector.get_list().filter(user=self.request.user)
        print(qs)
        OrderService.check_status_orders(qs)
        return qs


class OrderCreateAPIView(CreateAPIView):
    """
    """

    authentication_classes = [JWTAuthentication,]
    queryset = OrderSelector.get_list()
    serializer_class = OrderSerializer

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)