from api.serializers import SongCreateSerializer, SongSerializer
from api.viewsets import ListCreateViewSet
from app.models import Song


class SongViewSet(ListCreateViewSet):
    queryset = Song.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return SongCreateSerializer
        return SongSerializer
