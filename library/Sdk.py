#To do: move constants to conf

TOKEN_KEY = "thingspacecloud"
API_URL = "https://qa.vzwapi.dev.cloud.synchronoss.net:8443/cloud/"
AUTH_URL = "https://qa.vzwapi.dev.cloud.synchronoss.net:8443/"
CLIENT_KEY = "ck0908123456789067"
CLIENT_SECRET = "cs0908123456789067"
VERSION = "1"
REDIRECT_URI = 'http://localhost:8080'

from RESTClient import RESTClient
class Sdk():
    """
    The main Sdk class. Includes functions for authorization
    and other Sdk calls

    """

    def __init__(self):
        self.rest_client = RESTClient()

    def authorize(self):
        """
        Function to authorize with the API and generate the code
        """
        payload = {'client_id' : CLIENT_KEY, 'response_type' : 'code', 'redirect_uri' :
                   REDIRECT_URI}
        return self.rest_client.http_request(AUTH_URL + 'authorize', 'GET', payload)

    def token(self, code):
        """
        Use the code obtained in Auth flow to  create access token and refresh
        token

        Parameters:
            code    - (str) The code obtained from the Authorization flow
        """

        payload = {
            'client_id' : CLIENT_KEY,
            'client_secret' : CLIENT_SECRET,
            'code' : code,
            'grant_type': 'authorization_code',
            'redirect_uri' : REDIRECT_URI,
        }
        print AUTH_URL + 'token'
        print payload
        return self.rest_client.http_request(AUTH_URL + 'token', 'POST',
                                            payload)

    def refreshToken(self, refresh_token):
        """
        Use the refresh token  to obtain the access token

        Parameters:
            refresh_token   - (str) The Refresh token
        """
        payload = {
            'client_id' : CLIENT_KEY,
            'client_secret' : CLIENT_SECRET,
            'refresh_token' : refresh_token,
            'grant_type': 'refresh_token',
            'redirect_uri' : REDIRECT_URI,
        }
        print AUTH_URL + 'token'
        print payload
        return self.rest_client.http_request(AUTH_URL + 'token', 'POST',
                                            payload)
