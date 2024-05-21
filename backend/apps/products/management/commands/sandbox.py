
from django.core.management.base import BaseCommand

from backend.apps.products.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        qs = Product.objects.all()
        for p in qs:
            p.pk = None
            p.save()