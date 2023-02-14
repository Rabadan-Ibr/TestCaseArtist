from django.contrib import admin

from app.models import Album, Artist, Song, SongAlbumM2M


class SongsInAlbumInline(admin.TabularInline):
    model = SongAlbumM2M
    extra = 1


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist')


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'artist')
    inlines = (SongsInAlbumInline,)
