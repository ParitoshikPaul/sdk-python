from thingspace.env import Env
from thingspace.packages.requests.requests import Request

class Oauth():
    def get_authorize_url(self):
        req = Request(
            'GET',
            str(Env.api_cloud + '/oauth2/authorize'),
            params={
                'client_id': self.client_key,
                'redirect_uri': self.callback_url,
                'response_type': 'code',
            }
        )
        prepped = req.prepare()
        return prepped.url


    def token(self, auth_code):
        resp = self.networker(Request(
            'POST',
            str(Env.api_url + '/cloud/' + Env.api_version + '/oauth2/token'),
            data={
                'client_id': self.client_key,
                'client_secret': self.client_secret,
                'redirect_uri': self.callback_url,
                'code': auth_code,
                'grant_type': 'authorization_code',
            }
        ))

        json = resp.json()
        # need to handle error cases
        self.auth_token = json['access_token']
        self.refresh_token = json['refresh_token']
        self.authenticated = True

        return json