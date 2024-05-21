
from backend.apps.common.services import BaseSelector
from backend.apps.products.models import Product


class ProductSelector(BaseSelector):

    model = Product

    @classmethod
    def get_list(cls):
        return cls.get_queryset().prefetch_related("pictures").filter(is_published=True)