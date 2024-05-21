

class BaseSelector:
    """
    """

    model = None

    @classmethod
    def get_queryset(cls,):
        return cls.model.objects.all()
