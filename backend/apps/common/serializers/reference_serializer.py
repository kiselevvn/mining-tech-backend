from rest_framework.serializers import (
    CharField,
    PrimaryKeyRelatedField,
    Serializer,
)


class ReferenceSerializer(Serializer):
    """
    """
    id = PrimaryKeyRelatedField()
    name =  CharField(source="__str__")
    # class Meta:
    #     # fields = ["id", ]
    #     fields = "__all__"
