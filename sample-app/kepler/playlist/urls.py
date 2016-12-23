from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^playlists/(?P<uid>.*)', views.playlist_items, name='playlist_items'),
    url(r'^playlists', views.playlists, name='playlists'),
    url(r'^playlist/(?P<uid>.*)', views.playlist, name='playlists'),
    url(r'^updateplaylistform/(?P<uid>.*)', views.update_playlist_form, name='updateplaylistform'),
    url(r'^updateplaylistdefform/(?P<uid>.*)', views.update_playlist_def_form, name='updateplaylistitemform'),
    url(r'^updateplaylist/(?P<uid>.*)', views.update_playlist, name='updateplaylist'),
    url(r'^updateplaylistdef/(?P<uid>.*)', views.update_playlist_def, name='updateplaylistdef'),
    url(r'^deleteplaylist/(?P<uid>.*)', views.delete_playlist, name='deleteplaylist'),
    url(r'^deleteplaylistitem/(?P<uid>.*)/(?P<item_uid>.*)', views.delete_playlist_item, name='deleteplaylistitem'),
    url(r'^playlistform', views.playlistform, name='playlistform'),
    url(r'^createplaylistform', views.createplaylistform, name='createplaylistform'),
]