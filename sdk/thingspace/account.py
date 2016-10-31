from .api import cloud
from .RESTClient import RESTClient

class account(cloud):

    def __init__(self, access_token, destination_url):
        cloud.__init__(self)
        self.access_token = access_token
        self.destination_url = destination_url

    def getaccount(self):
        return self.rest_client.get(self.destination_url, {}, {'Authorization':  'Bearer ' +
                                                   self.access_token})

