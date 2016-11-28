from thingspace.models.struct import Struct


class UploadIntent(Struct):

    def __init__(self, checksum,  json):
        super(UploadIntent, self).__init__(json)

        if not self.uploadurls.get('commiturl', None):
            self.chunk = False
        else:
            self.chunk = True

        self.uploadurls['uploadurl'] += '&checksum=' + checksum
