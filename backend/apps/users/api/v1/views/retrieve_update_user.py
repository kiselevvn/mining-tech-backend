from rest_framework import serializers
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from backend.apps.users.models import Address, User


class AddressSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Address
        fields = [
            "id",
            "value",
        ]

class UserRetrieveUpdateSerializer(serializers.ModelSerializer):
    """
    Картинка товара
    """

    phone = serializers.CharField(required=False)
    addresses = AddressSerializer(many=True)

    def validate(self, data):
        """
        Check that the start is before the stop.
        """
        if "phone" in data and len(data.get("phone")) != 18:
            raise serializers.ValidationError("Номер телефона введен не верно")
        return data

    class Meta:
        model = User
        fields = [
            "email",
            "phone",
            "addresses",
        ]

    def update(self, instance, validated_data):
        address_list = validated_data.get("addresses", None)
        instance.phone = validated_data.get("phone", None)
        address_queryset = instance.addresses.all()

        created_ids = set(address_queryset.values_list("pk", flat=True))
        list_ids = {a.get("id") for a in address_list}
        removed_ids = created_ids - list_ids
        instance.addresses.filter(pk__in=removed_ids).delete()

        if address_list:
            for data in address_list:
                if "id" in data:
                    a = address_queryset.get(pk=data.get("id"))
                    a.value = data.get("value")
                    a.save()
                else:
                    a = Address(
                        user=instance,
                        value=data.get("value")
                    )
                    a.save()

        instance.save()
        return instance


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    """
    """

    queryset = User.objects.prefetch_related("addresses")
    serializer_class = UserRetrieveUpdateSerializer
    authentication_classes = [JWTAuthentication,]


    def get_object(self):
        """
        """
        print(self.request.user)
        # queryset = self.filter_queryset(self.get_queryset())

        # # Perform the lookup filtering.
        # lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        # assert lookup_url_kwarg in self.kwargs, (
        #     'Expected view %s to be called with a URL keyword argument '
        #     'named "%s". Fix your URL conf, or set the `.lookup_field` '
        #     'attribute on the view correctly.' %
        #     (self.__class__.__name__, lookup_url_kwarg)
        # )

        # filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        # obj = get_object_or_404(queryset, **filter_kwargs)

        # # May raise a permission denied
        # self.check_object_permissions(self.request, obj)

        return self.request.user