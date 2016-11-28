from thingspace.models.struct import Struct


class CloudFolder(Struct):

    def __init__(self, json):
        super(CloudFolder, self).__init__(json)


    def fullpath(self):
        if self.parent_path == '/':
            return '/' + self.name
        else:
            return self.parent_path + '/' + self.name
