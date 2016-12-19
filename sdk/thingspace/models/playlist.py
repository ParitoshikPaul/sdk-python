from thingspace.models.struct import Struct


class Playlist(Struct):

    def __init__(self, json):
        super(Playlist, self).__init__(json)
