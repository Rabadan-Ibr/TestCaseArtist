from api.serializers import AlbumCreateSerializer, AlbumSerializer
from api.viewsets import ListCreateViewSet
from app.models import Album


class AlbumViewSet(ListCreateViewSet):
    """
    Создание альбома и отображение списка альбомов.
    """
    queryset = Album.objects.select_related(
        'artist',
    ).prefetch_related('songs_m2m__song')

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AlbumCreateSerializer
        return AlbumSerializer
