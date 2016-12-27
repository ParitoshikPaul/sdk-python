from thingspace.env import Env
from thingspace.models.factories.fops_factories import FopsFactories
from thingspace.packages.requests.requests import Request
from thingspace.exceptions import CloudError, NotFoundError, ConflictError
from thingspace.models.factories.playlist_factories import PlaylistFactories
from thingspace.packages.requests.requests.packages.urllib3.packages.six.moves import urllib

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

        if resp.status_code != 200:
            raise CloudError("Could not get playlists", response=resp)

        json = resp.json()

        playlists = PlaylistFactories.playlists_from_json(json['playlistDefinitions'].get('playlistDefinition', []))

        return playlists

    def playlist(self, playlist_uid):
        if not self.authenticated:
            return None

        headers = {
            "Authorization": "Bearer " + self.access_token
        }
        resp = self.networker(Request(
            'GET',
            Env.api_url + '/cloud/' + Env.api_version + '/playlists/' + playlist_uid,
            headers=headers
        ))

        if resp.status_code != 200:
            raise CloudError("Could not get playlists", response=resp)

        json = resp.json()
        playlist = PlaylistFactories.playlist_from_json(json['playlistDefinition'])
        return playlist

    def playlist_items(self, playlistUid='', page='', count='', sort=''):
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

        if resp.status_code != 200:
            raise CloudError("Could not get playlists", response=resp)

        json = resp.json()
        files = PlaylistFactories.playlist_items_from_json(self, playlistUid,
                                                           json['playlist'].get('playlistElement', []))
        return files

    def playlist_item_download_url(self, playlist_item=None, playlist_uid=None, item_uid=None):
        if not self.authenticated:
            return None

        if (playlist_item):
            playlist_uid = playlist_item.playlist_uid
            item_uid = playlist_item.itemuid

        req = Request(
            'GET',
            Env.api_cloud + '/playlists/' + urllib.parse.quote(playlist_uid) + '/items/' + urllib.parse.quote(item_uid),
            params={
                'access-token': self.access_token
            }
        )
        prepped = req.prepare()
        return prepped.url

    def create_playlist(self, name, paths, type):
        if not self.authenticated:
            return None

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

    def create_playlist_items(self, playlist_uid="",  playlistItems=[]):
        if not self.authenticated:
            return None

        #add mandatory
        body = {
            'add': playlistItems
        }


        resp = self.networker(Request(
            'POST',
            Env.api_cloud + '/playlists' + playlist_uid + 'items',
            json=body,
            headers={
                "Authorization": "Bearer " + self.access_token
            }
        ))

        json = resp.json()
        return json

    def delete_playlist(self, playlist_uid=""):
        if not self.authenticated:
            return None

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
        if not self.authenticated:
            return None

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

    def update_playlist(self, playlist_uid, name="", type=""):
        if not self.authenticated:
            return None
        body = {
            'name': name,
            'type': type
        }
        resp = self.networker(Request(
            'PUT',
            Env.api_cloud + '/playlists/' + playlist_uid,
            json=body,
            headers={
                "Authorization": "Bearer " + self.access_token
            }
        ))

        if resp.status_code == 404:
            raise NotFoundError("Playlist Item not found", response=resp)

        if resp.status_code != 200:
            raise CloudError("Could not delete playlist item", response=resp)

            return resp.json

    def update_playlist_def(self, playlist_uid, name="", paths="", type=""):
        if not self.authenticated:
            return None
        body = {
            'name': name,
            'paths': paths,
            'type': type
        }
        resp = self.networker(Request(
            'PUT',
            Env.api_cloud + '/playlists/' + playlist_uid + '/items',
            json=body,
            headers={
                "Authorization": "Bearer " + self.access_token
            }
        ))

        if resp.status_code == 404:
            raise NotFoundError("Playlist Item not found", response=resp)

        if resp.status_code != 200:
            raise CloudError("Could not delete playlist item", response=resp)

            return resp.json

