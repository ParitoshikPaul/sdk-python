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


