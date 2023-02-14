from rest_framework import serializers

from app.models import Artist, Song, SongAlbumM2M


class SongCreateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=150)
    artist = serializers.PrimaryKeyRelatedField(queryset=Artist.objects.all())

    class Meta:
        model = Song
        fields = ('title', 'artist')


class SongArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'name')


class SongSerializer(serializers.ModelSerializer):
    artist = SongArtistSerializer()

    class Meta:
        model = Song
        fields = ('title', 'artist')


class SongViaAlbumSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='song.title', read_only=True)
    position = serializers.IntegerField(read_only=True)

    class Meta:
        model = SongAlbumM2M
        fields = ('title', 'position')
