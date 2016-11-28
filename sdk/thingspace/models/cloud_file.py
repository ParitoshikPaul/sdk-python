from thingspace.models.struct import Struct


class CloudFile(Struct):

    def __init__(self, cloud, json):
        super(CloudFile, self).__init__(json)
        self.cloud = cloud

    def download_url(self):
        return self.cloud.download_url(self)

    def fullpath(self):
        return self.parent_path + '/' + self.name
