from thingspace.models.struct import Struct


class CloudFolder(Struct):

    def __init__(self, json):
        super(CloudFolder, self).__init__(json)
