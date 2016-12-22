from thingspace.models.struct import Struct


class PlaylistItem(Struct):

    def __init__(self, cloud, playlist_uid, json):
        super(PlaylistItem, self).__init__(json)
        self.cloud = cloud
        self.playlist_uid = playlist_uid

    def download_url(self):
        return self.cloud.playlist_item_download_url(self)