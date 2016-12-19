from thingspace.models.playlist import Playlist


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


