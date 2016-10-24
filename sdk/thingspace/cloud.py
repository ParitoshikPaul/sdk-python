from ..packages.requests.requests import Request, Session


class Cloud:
    api_url = 'https://api.cloudapi.verizon.com'

    def __init__(self,
                 client_key,
                 client_secret,
                 callback_url,
                 auth_token=None,
                 refresh_token=None
                 ):
        self.client_key = client_key
        self.client_secret = client_secret
        self.callback_url = callback_url
        self.auth_token = auth_token
        self.refresh_token = refresh_token

        # authenticated if we have an auth token
        self.authenticated = self.auth_token is not None

    def get_authorize_url(self):
        req = Request(
            'GET',
            str(Cloud.api_url + '/cloud/1/oauth2/authorize'),
            params={
                'client_id': self.client_key,
                'redirect_uri': self.callback_url,
                'response_type': 'code',
            }
        )
        prepped = req.prepare()
        return prepped.url

    def token(self, auth_code):
        s = Session()
        req = Request(
            'POST',
            str(Cloud.api_url + '/cloud/1/oauth2/token'),
            data={
                'client_id': self.client_key,
                'client_secret': self.client_secret,
                'redirect_uri': self.callback_url,
                'code': auth_code,
                'grant_type': 'authorization_code',
            }
        )
        prepped = req.prepare()

        resp = s.send(prepped);

        #need to set tokens here

        return resp.json()

    def fullview(self):
        if not self.authenticated:
            return None

        s = Session()
        req = Request(
            'GET',
            str(Cloud.api_url + '/cloud/1/fullview'),
            headers={
                "Authorization" : "Bearer " + self.auth_token
            }
        )

        prepped = req.prepare()
        resp = s.send(prepped)
        return resp.json()
