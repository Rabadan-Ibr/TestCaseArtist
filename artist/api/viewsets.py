from rest_framework.viewsets import GenericViewSet, mixins


class CreateViewSet(mixins.CreateModelMixin, GenericViewSet):
    pass


class ListCreateViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericViewSet,
):
    pass
