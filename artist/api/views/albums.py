from api.serializers import AlbumCreateSerializer, AlbumSerializer
from api.viewsets import ListCreateViewSet
from app.models import Album


class AlbumViewSet(ListCreateViewSet):
    queryset = Album.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AlbumCreateSerializer
        return AlbumSerializer