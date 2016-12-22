from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^playlists/(?P<uid>.*)', views.playlist_items, name='playlist_items'),
    url(r'^playlists', views.playlists, name='playlists'),
    url(r'^playlist/(?P<uid>.*)', views.playlist, name='playlists'),
    url(r'^updateplaylistform/(?P<uid>.*)', views.update_playlist_form, name='updateplaylistform'),
    url(r'^updateplaylist/(?P<uid>.*)', views.update_playlist, name='updateplaylistform'),
    url(r'^playlistform', views.playlistform, name='playlistform'),
    url(r'^createplaylistform', views.createplaylistform, name='createplaylistform'),
]