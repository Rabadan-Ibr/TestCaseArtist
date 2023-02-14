from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import AlbumViewSet, ArtistViewSet, SongViewSet

app_name = 'api'


router_v1 = DefaultRouter()
router_v1.register('artists', ArtistViewSet, basename='artists')
router_v1.register('songs', SongViewSet, basename='songs')
router_v1.register('albums', AlbumViewSet, basename='albums')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
