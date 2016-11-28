from thingspace.env import Env
from thingspace.exceptions import UnauthorizedError
from thingspace.models.token import Token
from thingspace.packages.requests.requests import Request


class Oauth():
    def authorize_url(self):
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
        ), auto_refresh=False)

        if resp.status_code != 200:
            raise UnauthorizedError('Could not get access tokens please reauthenticate', response=resp)

        json = resp.json()
        self.access_token = json['access_token']
        self.refresh_token = json['refresh_token']
        self.authenticated = True

        return Token(json)

    def refresh(self):
        if not self.refresh_token:
            raise ValueError("SDK does not have any refresh token, cant refresh")

        resp = self.networker(Request(
            'POST',
            str(Env.api_url + '/cloud/' + Env.api_version + '/oauth2/token'),
            data={
                'client_id': self.client_key,
                'client_secret': self.client_secret,
                'redirect_uri': self.callback_url,
                'refresh_token': self.refresh_token,
                'grant_type': 'refresh_token',
            }
        ), auto_refresh=False)

        if resp.status_code != 200:
            raise UnauthorizedError('Could not refresh tokens please reauthenticate', response=resp)

        json = resp.json()

        self.access_token = json['access_token']
        self.refresh_token = json['refresh_token']
        self.authenticated = True

        token_response = Token(json)

        #callback
        if callable(self.on_refreshed):
            self.on_refreshed(token_response)

        return token_response


