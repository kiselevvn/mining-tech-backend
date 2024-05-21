from rest_framework.serializers import (
    CharField,
    ModelSerializer,
    SerializerMethodField,
)

from backend.apps.products import models


class ProductPictureSerializer(ModelSerializer):
    """
    Картинка товара
    """

    class Meta:
        model = models.Picture
        # fields = ["id", ]
        fields = "__all__"


class ProductSerializer(ModelSerializer):
    """
    Товар
    """

    # pictures = ProductPictureSerializer(many=True, read_only=True)

    # category_id = CharField(source="category.id", required=False, write_only=True)
    category = CharField(source="category.name", required=False, read_only=True)
    brand = CharField(required=False, read_only=True)
    algorithm = CharField(required=False, read_only=True)
    currency_mining = CharField(required=False, read_only=True)
    hashrate = CharField(required=False, read_only=True)
    power = CharField(required=False, read_only=True)
    main_picture = SerializerMethodField()

    class Meta:
        model = models.Product
        fields = [
            "id",
            "name",
            "price",
            "short_description",
            # "category_id",
            "category",
            # "brand_id",
            "brand",
            # "algorithm_id",
            "algorithm",
            # "currency_mining_id",
            "currency_mining",
            # "hashrate_id",
            "hashrate",
            # "power_id",
            "power",

            "is_available",
            "is_pre_order",
            # "pictures",
            "main_picture"
        ]

    def get_main_picture(self, obj):
        request = self.context.get('request')
        mains = obj.pictures.filter(is_main=True)
        if mains.count() > 0:
            return request.build_absolute_uri(mains.first().image.url)
        return None