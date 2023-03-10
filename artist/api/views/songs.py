from api.serializers import SongCreateSerializer, SongSerializer
from api.viewsets import ListCreateViewSet
from app.models import Song


class SongViewSet(ListCreateViewSet):
    """
    Создание песни и отображение списка песен
    """
    queryset = Song.objects.select_related('artist')

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return SongCreateSerializer
        return SongSerializer
