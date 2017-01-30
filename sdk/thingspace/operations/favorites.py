from thingspace.env import Env
from thingspace.packages.requests.requests import Request
from thingspace.exceptions import CloudError, NotFoundError, ConflictError
class Favorites():

    def favorites(self, virtualfolder='', type='', filetype=''):
        if not self.authenticated:
            return None

        headers = {
            "Authorization": "Bearer " + self.access_token
        }
        params = {
            "virtualfolder": virtualfolder,
            "type": type,
            "filetype": filetype,
        }
        resp = self.networker(Request(
            'GET',
            Env.api_url + '/cloud/' + Env.api_version + '/favorites',
            headers=headers, params=params
        ))

        json = resp.json()
        return json

    def updatefavorites(self, uri, createversion):
        if not self.authenticated:
            return None

        headers = {
            "Authorization": "Bearer " + self.access_token
        }
        body = {
            "uri": uri,
            "createversion": createversion,
        }
        resp = self.networker(Request(
            'PUT',
            Env.api_url + '/cloud/' + Env.api_version + '/favorites',
            json=body,
            headers=headers,
        ))

        json = resp.json()
        return json

    def deletefavorites(self, uri, createversion):
        if not self.authenticated:
            return None

        headers = {
            "Authorization": "Bearer " + self.access_token
        }
        body = {
            "uri": uri,
            "createversion": createversion,
        }
        resp = self.networker(Request(
            'PUT',
            Env.api_url + '/cloud/' + Env.api_version + '/favorites',
            headers=headers, body=body
        ))

        json = resp.json()
        return json