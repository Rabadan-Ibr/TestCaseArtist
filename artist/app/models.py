from django.db import models

from app.utils import year_max


class Artist(models.Model):
    name = models.CharField(verbose_name='artist Name', max_length=150)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Artist'

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(verbose_name='song title', max_length=150)
    artist = models.ForeignKey(
        'Artist',
        verbose_name='artist',
        on_delete=models.CASCADE,
        related_name='songs',
    )

    class Meta:
        ordering = ('title',)
        verbose_name = 'Song'

    def __str__(self):
        return self.title


class SongAlbumM2M(models.Model):
    song = models.ForeignKey(
        'Song',
        on_delete=models.CASCADE,
        related_name='albums_m2m',
    )
    album = models.ForeignKey(
        'Album',
        on_delete=models.CASCADE,
        related_name='songs_m2m',
    )
    position = models.PositiveSmallIntegerField(verbose_name='position')

    class Meta:
        ordering = ('position',)
        constraints = [
            models.UniqueConstraint(
                fields=['song', 'album', 'position'],
                name='unique_song_album',
            )
        ]


class Album(models.Model):
    title = models.CharField(
        verbose_name='album title',
        max_length=150,
        unique=True,
    )
    year = models.PositiveSmallIntegerField(verbose_name='year')
    artist = models.ForeignKey(
        'Artist',
        verbose_name='artist',
        on_delete=models.CASCADE,
        related_name='albums',
    )
    songs = models.ManyToManyField(
        'Song',
        verbose_name='songs',
        through='SongAlbumM2M',
        related_name='albums',
    )

    class Meta:
        ordering = ('title',)
        verbose_name = 'Album'
        constraints = (
            models.CheckConstraint(
                check=models.Q(year__lte=year_max()),
                name='year_check',
            ),
        )

    def __str__(self):
        return f'{self.title}, {self.artist.name}'
