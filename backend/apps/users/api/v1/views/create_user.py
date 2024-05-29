from rest_framework import serializers
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from backend.apps.orders import models
from backend.apps.users.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    """
    Картинка товара
    """

    username = serializers.CharField()
    password = serializers.CharField()


    class Meta:
        model = User
        fields = [
            "username",
            "password",
        ]

    def create(self, validated_data):
        u = User.objects.create_user(
            username=validated_data.get("username").lower(),
            email=validated_data.get("username").lower(),
            password=validated_data.get("password")
        )
        u.is_active = True
        u.save()
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

