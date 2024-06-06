from rest_framework import serializers
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from backend.apps.orders import models
from backend.apps.users.models import Address, User


class UserCreateSerializer(serializers.ModelSerializer):
    """
    Картинка товара
    """

    username = serializers.CharField()
    password = serializers.CharField()
    phone = serializers.CharField(required=False)
    address = serializers.CharField(required=False)

    def validate(self, data):
        """
        Check that the start is before the stop.
        """
        if User.objects.filter(username=data.get("username")).count() > 0:
            raise serializers.ValidationError("Электронная почта уже зарегестрирована")
        if "phone" in data and len(data.get("phone")) != 18:
            raise serializers.ValidationError("Номер телефона введен не верно")
        return data

    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "phone",
            "address",
        ]

    def create(self, validated_data):
        validated_data.get("address")
        u = User.objects.create_user(
            username=validated_data.get("username").lower(),
            email=validated_data.get("username").lower(),
            password=validated_data.get("password"),
            phone=validated_data.get("phone", None),
        )
        u.is_active = True
        u.save()
        if validated_data.get("address", False):
            address = Address(user=u, value=validated_data.get("address"))
            address.save()
        return u
        # return OrderService.create(
        #     validated_data=validated_data.get,
        #     user=self.context.get("request").user
        # )

class UserCreateAPIView(CreateAPIView):
    """
    """

    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

