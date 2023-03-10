from rest_framework import serializers

from app.models import Artist

from .albums import AlbumSerializer


class ArtistCreateSerializer(serializers.ModelSerializer):
    """
    Сериализатор для создания исполнителя.
    """
    name = serializers.CharField(max_length=150)

    class Meta:
        model = Artist
        fields = ('name',)


class ArtistSerializer(serializers.ModelSerializer):
    """
    Сериализатор отображения исполнителя вместе с альбомами.
    """
    name = serializers.CharField(read_only=True)
    albums = AlbumSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ('name', 'albums')
