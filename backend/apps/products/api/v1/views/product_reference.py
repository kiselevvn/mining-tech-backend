from rest_framework import serializers
from rest_framework.generics import ListAPIView

from backend.apps.common.models import (
    Algorithm,
    Brand,
    CurrencyMining,
    Hashrate,
    Power,
)


class ProductReferenceSerializer(serializers.Serializer):

    name = serializers.CharField()
    items = serializers.ListField()



class ProductReferenceListAPIView(ListAPIView):
    """
    """

    serializer_class = ProductReferenceSerializer
    authentication_classes = []
    permission_classes = []

    def get_queryset(self):
        get_items = lambda model: [{"id": o.pk, "name": o.__str__()}for o in model.objects.all()]
        return [
            {
                "name":"algorithm",
                "items": get_items(Algorithm)
            },
            {
                "name":"brand",
                "items": get_items(Brand)
            },
            {
                "name":"currency_mining",
                "items": get_items(CurrencyMining)
            },
            {
                "name":"hashrate",
                "items": get_items(Hashrate)
            },
            {
                "name":"power",
                "items": get_items(Power)
            },
        ]


