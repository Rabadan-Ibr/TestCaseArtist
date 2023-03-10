from api.serializers import ArtistCreateSerializer, ArtistSerializer
from api.viewsets import ListCreateViewSet
from app.models import Artist


class ArtistViewSet(ListCreateViewSet):
    """
    Создание исполнителя и отображение списка исполнителей.
    """
    queryset = Artist.objects.prefetch_related('albums__songs_m2m__song')

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == 'POST':
            return ArtistCreateSerializer
        return ArtistSerializer
