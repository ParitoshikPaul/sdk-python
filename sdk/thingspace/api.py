import requests, json
import sys
from RESTClient import RESTClient

class cloud():
    def __init__(self):
        self.client_id = None
        self.client_secret = None
        self.callback_url = None
        self.auth_url = None
        self.api_url = None
        self.token_file = None
        self.refresh_token = None
        self.access_token = None
        self.token_expires = None
        self.isauthorized = False
        self.rest_client = RESTClient()

    def testfunc(self):
        return "Just a test"

    def set_config_data(self, client_key, client_secret, callback_url, auth_url,
                        api_url, api_version):
        self.client_key = client_key
        self.client_secret = client_secret
        self.callback_url = callback_url
        self.auth_url = auth_url
        self.api_url = api_url

        return True

    def load_config_from_file(self, config_path):
        try:
            config = json.loads(open(config_path).read())
            self.client_id = config['client_id']
            self.client_key = config['client_key']
            self.callback_url = config['callback_url']
            self.auth_url = config['auth_url']
            self.api_url = config['api_url']
            self.api_version = config['api_version']
            self.token_file = config['token_file']
        except KeyError:
            print("Config file incomplete, please recheck configuration")
            sys.exit(-1)
        return True

    def load_tokens(self):
        try:
            token_data = json.loads(open(self.token_file).read())
            if not cloud.timestamp_compare(token_data['token_expires']):
                return False
            self.access_token = token_data['access_token']
            self.refresh_token = token_data['refresh_token']
            self.token_expires = token_data['token_expires']
        except:
            print("Unable to read token data")
            sys.exit(-1)
        return True

    def set_token_data(self, access_token, refresh_token, token_expires):
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.token_expires = token_expires
        return True

    def write_token_data(self):
        file_handle = open(self.token_file, 'w')
        token_data = {
                'refresh_token': self.refresh_token,
                'access_token': self.access_token,
                'token_expires': self.token_expires,
                }
        file_handle.write(json.dumps(token_data))

        return True

