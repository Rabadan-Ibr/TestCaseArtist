from rest_framework import serializers

from app.models import Artist, Song


class SongCreateSerializer(serializers.ModelSerializer):
    """
    Сериализатор для создания песни.
    """
    title = serializers.CharField(max_length=150)
    artist = serializers.PrimaryKeyRelatedField(queryset=Artist.objects.all())

    class Meta:
        model = Song
        fields = ('title', 'artist')


class SongArtistSerializer(serializers.ModelSerializer):
    """
    Сериализатор исполнителя при отображении песни.
    """
    class Meta:
        model = Artist
        fields = ('id', 'name')


class SongSerializer(serializers.ModelSerializer):
    """
    Сериализатор отображения песни.
    """
    artist = SongArtistSerializer()

    class Meta:
        model = Song
        fields = ('title', 'artist')
