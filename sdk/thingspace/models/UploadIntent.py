class UploadIntent:

    def __init__(self, checksum,  **entries):
        self.__dict__.update(entries)

        if not self.uploadurls.get('commiturl', None):
            self.chunk = False
        else:
            self.chunk = True

        self.uploadurls['uploadurl'] += '&checksum=' + checksum


    def __repr__(self):
        return '<%s>' % str('\n '.join('%s : %s' % (k, repr(v)) for (k, v) in self.__dict__.items()))
