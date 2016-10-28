from api import cloud
from urllib import urlencode
from RESTClient import RESTClient

class auth(cloud):
    """
    The main auth class. Includes functions for authorization

    """

    def __init__(self):
        cloud.__init__(self)

    def authorize(self):
        """
        Function to authorize with the API and generate the code
        """
        payload = {'client_id' : self.client_key, 'response_type' : 'code', 'redirect_uri' :
                   self.callback_url}
        return self.auth_url + 'authorize?' + urlencode(payload)

    def token(self, code):
        """
        Use the code obtained in Auth flow to  create access token and refresh
        token

        Parameters:
            code    - (str) The code obtained from the Authorization flow
        """

        payload = {
            'client_id' : self.client_key,
            'client_secret' : self.client_secret,
            'code' : code,
            'grant_type': 'authorization_code',
            'redirect_uri' : self.callback_url,
        }
        #return str(payload)
        return self.rest_client.http_request(self.auth_url+ 'token', 'POST',
                                            payload)

    def refreshToken(self, refresh_token):
        """
        Use the refresh token  to obtain the access token

        Parameters:
            refresh_token   - (str) The Refresh token
        """
        payload = {
            'client_id' : self.client_key,
            'client_secret' : self.client_secret,
            'refresh_token' : refresh_token,
            'grant_type': 'refresh_token',
            'redirect_uri' : self.callback_url,
        }
        return self.rest_client.http_request(self.auth_url + 'token', 'POST',
                                            payload)
