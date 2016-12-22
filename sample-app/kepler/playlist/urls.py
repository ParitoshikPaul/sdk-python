from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^playlists/(?P<uid>.*)', views.playlist_items, name='playlist_items'),
    url(r'^playlists', views.playlist, name='playlists'),
    url(r'^playlistform', views.playlistform, name='playlistform'),
    url(r'^createplaylistform', views.createplaylistform, name='createplaylistform'),
]