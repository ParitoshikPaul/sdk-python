from thingspace.models.struct import Struct


class Account(Struct):

    def __init__(self, json):
        super(Account, self).__init__(json)
