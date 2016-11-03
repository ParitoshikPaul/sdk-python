class CloudFile:

    def __init__(self, cloud, **entries):
        self.cloud = cloud
        self.__dict__.update(entries)

    def __repr__(self):
        return '<%s>' % str('\n '.join('%s : %s' % (k, repr(v)) for (k, v) in self.__dict__.items()))

    def download_url(self):
        return self.cloud.download_url(self)

