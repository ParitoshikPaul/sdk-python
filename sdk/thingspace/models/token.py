from thingspace.models.struct import Struct


class Token(Struct):
    def __init__(self, json):
        super(Token, self).__init__(json)
