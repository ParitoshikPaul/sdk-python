from thingspace.env import Env
from thingspace.packages.requests.requests import Request
from thingspace.exceptions import CloudError, NotFoundError, ConflictError


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

    def get_playlist_definition(self, playlistUid=''):
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

    def get_playlist_items_content(self, playlistUid='', item_uid=''):
        if not self.authenticated:
            return None

        headers = {
            "Authorization": "Bearer " + self.access_token
        }
        resp = self.networker(Request(
            'GET',
            Env.api_url + '/cloud/' + Env.api_version + '/playlists/' + playlistUid + '/items' + item_uid,
            headers=headers
        ))

        playlist_items_content = resp.json()
        return playlist_items_content

    def create_playlist(self, name="", paths="", type=""):

        #add mandatory
        body = {
            'name': name,
            'paths': paths,
            'type': type,
        }


        resp = self.networker(Request(
            'POST',
            Env.api_cloud + '/playlists',
            json=body,
            headers={
                "Authorization": "Bearer " + self.access_token
            }
        ))

        json = resp.json()
        return json

    def delete_playlist(self, playlist_uid=""):

        resp = self.networker(Request(
            'DELETE',
            Env.api_cloud + '/playlists/' + playlist_uid,
            headers={
                "Authorization": "Bearer " + self.access_token
            }
        ))

        if resp.status_code == 404:
            raise NotFoundError("Playlist not found", response=resp)

        if resp.status_code != 200:
            raise CloudError("Could not delete playlist", response=resp)

            return

    def delete_playlist_item(self, playlist_uid="", item_uid=""):

        resp = self.networker(Request(
            'DELETE',
            Env.api_cloud + '/playlists/' + playlist_uid + '/items/' + item_uid,
            headers={
                "Authorization": "Bearer " + self.access_token
            }
        ))

        if resp.status_code == 404:
            raise NotFoundError("Playlist Item not found", response=resp)

        if resp.status_code != 200:
            raise CloudError("Could not delete playlist item", response=resp)

            return

