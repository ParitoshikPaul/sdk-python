from api import cloud
from RESTClient import RESTClient

class fops(cloud):

    def __init__(self, access_token, destination_url):
        cloud.__init__(self)
        self.access_token = access_token
        self.destination_url = destination_url

    def get_fileupload_intent(self, path, name, size, checksum, chunk=False):
        return self.rest_client.get(self.destination_url + '/fileupload/intent', 
                                {'path': path, 'name':
                                                       name, 'size': size,
                                                       'checksum': checksum}, 
                                {'Authorization':  'Bearer ' +
                                                   self.access_token})

    def fullview(self):
        return self.rest_client.get(self.destination_url + '/fullview', {},
                                    {'Authorization': 'Bearer ' +
                                     self.access_token})
