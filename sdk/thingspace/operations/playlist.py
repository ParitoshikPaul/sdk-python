from thingspace.env import Env
from thingspace.packages.requests.requests import Request




class Playlists():

    def playlists(self, type='', page='', count='', sort=''):
        if not self.authenticated:
            return None

        headers = {
            "Authorization": "Bearer " + self.access_token
        }
        params = {
            "type": type,
            "page": page,
            "count": count,
            "sort": sort,
        }
        resp = self.networker(Request(
            'GET',
            Env.api_url + '/cloud/' + Env.api_version + '/playlists',
            headers=headers, params=params
        ))

        playlist = resp.json()
        return playlist

    def get_playlist(self, playlistUid=''):
        if not self.authenticated:
            return None

        headers = {
            "Authorization": "Bearer " + self.access_token
        }
        resp = self.networker(Request(
            'GET',
            Env.api_url + '/cloud/' + Env.api_version + '/playlists/' + playlistUid,
            headers=headers
        ))

        playlist_uid = resp.json()
        return playlist_uid

    def get_playlist_items(self, playlistUid='', page='', count='', sort=''):
        if not self.authenticated:
            return None

        headers = {
            "Authorization": "Bearer " + self.access_token
        }
        params = {
            "page": page,
            "count": count,
            "sort": sort,
        }
        resp = self.networker(Request(
            'GET',
            Env.api_url + '/cloud/' + Env.api_version + '/playlists/' + playlistUid + '/items',
            headers=headers, params=params
        ))

        playlist_items = resp.json()
        return playlist_items



