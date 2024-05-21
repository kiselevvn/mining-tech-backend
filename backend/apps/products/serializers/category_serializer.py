from rest_framework.serializers import ModelSerializer

from backend.apps.products import models


class CategorySerializer(ModelSerializer):
    """
    Картинка товара
    """

    class Meta:
        model = models.Category
        # fields = ["id", ]
        fields = "__all__"
