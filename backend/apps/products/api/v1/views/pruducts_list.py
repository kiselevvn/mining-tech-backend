import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from backend.apps.products.models import Product
from backend.apps.products.selectors import ProductSelector
from backend.apps.products.serializers import ProductSerializer


class Pagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50

class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    price = django_filters.NumberFilter()
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')

    brand = django_filters.CharFilter(method="split_list_field")
    algorithm = django_filters.CharFilter(method="split_list_field")
    currency_mining = django_filters.CharFilter(method="split_list_field")
    hashrate = django_filters.CharFilter(method="split_list_field")
    power = django_filters.CharFilter(method="split_list_field")
    category = django_filters.CharFilter(method="split_list_field")

    class Meta:
        model = Product
        fields = [
            'name',
            'price',
            'category',
            'brand',
            'algorithm',
            'currency_mining',
            'hashrate',
            'power',
            'is_available',
            'is_pre_order',
            # 'release_date',
            # 'manufacturer'
            ]

    def split_list_field(self, queryset, field_name, value):
        filter_data = {
            f"{field_name}__in": [int(i) for i in value.split("-")[:-1]]
        }
        return queryset.filter(**filter_data)

class ProductListAPIView(ListAPIView):
    """
    """

    queryset = ProductSelector.get_list()
    serializer_class = ProductSerializer
    pagination_class = Pagination
    filter_class = ProductFilter
    filter_backends = [DjangoFilterBackend]
    authentication_classes = []
    permission_classes = []
