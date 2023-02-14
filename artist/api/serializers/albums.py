from django.db.transaction import atomic
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from api.validators import max_year, songs_validator
from app.models import Album, Artist, Song, SongAlbumM2M

from .songs import SongViaAlbumSerializer


class AlbumSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=150, read_only=True)
    artist = serializers.CharField(source='artist.name', read_only=True)
    year = serializers.IntegerField(read_only=True)
    songs = SongViaAlbumSerializer(
        many=True,
        source='songs_m2m',
        read_only=True,
    )

    class Meta:
        model = Album
        fields = ('artist', 'title', 'year', 'songs')


class AlbumSongsPositionsSerializer(serializers.ModelSerializer):
    song = serializers.PrimaryKeyRelatedField(
        queryset=Song.objects.all(),
        source='song.id',
    )
    position = serializers.IntegerField(min_value=1)

    class Meta:
        model = SongAlbumM2M
        fields = ('song', 'position')


class AlbumCreateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=150)
    year = serializers.IntegerField()
    artist = serializers.PrimaryKeyRelatedField(queryset=Artist.objects.all())
    songs = AlbumSongsPositionsSerializer(many=True, source='songs_m2m')

    class Meta:
        model = Album
        fields = ('title', 'year', 'artist', 'songs')
        validators = (
            UniqueTogetherValidator(
                queryset=Album.objects.all(),
                fields=('title', 'artist'),
                message='artist`s album title must be unique',
            ),
            max_year,
            songs_validator
        )

    @staticmethod
    def _add_songs(instance, songs_data):
        for song_data in songs_data:
            song = song_data.get('song').get('id')
            position = song_data.get('position')
            instance.songs.add(song, through_defaults={'position': position})
        return instance

    @atomic
    def create(self, validated_data):
        songs_data = validated_data.pop('songs_m2m')
        instance = super().create(validated_data)
        return self._add_songs(instance, songs_data)
