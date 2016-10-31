from .api import cloud
from .RESTClient import RESTClient

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

    def fileview(self, path):
        return self.rest_client.get(self.destination_url + '/metadata',
                                    {'path': path}, {'Authorization': 'Bearer '
                                                     + self.access_token})

    def getfile(self, path):
        return self.rest_client.get(self.destination_url + '/files/' +path, {},
                                    {'Authorization': 'Bearer '+
                                     self.access_token}, False)

    def gettrash(self, virtualfolder):
        return self.rest_client.get(self.destination_url + '/trash',
                                    {'virtualfolder': virtualfolder},
                                    {'Authorization': 'Bearer ' +
                                     self.access_token})
    def thumbnails(self, content_token):
        return self.rest_client.get(self.destination_url + '/thumbnails/' +
                                    content_token, {}, {'Authorization':
                                                        'Bearer '+ self.access_token})

    def newfileview(self, path):
        return {'data': 'New data'}
