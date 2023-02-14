from api.serializers import ArtistCreateSerializer, ArtistSerializer
from api.viewsets import ListCreateViewSet
from app.models import Artist


class ArtistViewSet(ListCreateViewSet):
    queryset = Artist.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == 'POST':
            return ArtistCreateSerializer
        return ArtistSerializer
