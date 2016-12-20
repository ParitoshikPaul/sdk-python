from thingspace.models.playlist import Playlist
from thingspace.models.playlist_item import PlaylistItem


class PlaylistFactories:

    @staticmethod
    def playlist_from_json(json):

        return Playlist(json)

    @staticmethod
    def playlists_from_json(json):
        playlists = []
        for playlist in json:
            playlists.append(PlaylistFactories.playlist_from_json(playlist))
        return playlists


    @staticmethod
    def playlist_item_from_json(cloud, playlist_uid, json):
        return PlaylistItem(cloud, playlist_uid, json)


    @staticmethod
    def playlist_items_from_json(cloud, playlist_uid, json):
        playlist_items = []
        for playlist_item in json:
            playlist_items.append(PlaylistFactories.playlist_item_from_json(cloud, playlist_uid, playlist_item))
        return playlist_items
