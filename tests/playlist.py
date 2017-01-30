#!/usr/bin/env python
import sys
from utils import Utils
import unittest
from thingspace.exceptions import CloudError, NotFoundError

cloud = Utils.cloud()

class Playlist(unittest.TestCase):

    def test_playlists(self):
        playlists = cloud.playlists(type='music', page='1', count='1', sort='name+asc')
        Utils.assert_is_playlist(self, playlists);
        self.assertTrue(playlists)

    def test_playlist(self):
        playlist = cloud.playlist(playlist_uid="98015ae9c2bb4d0d986693d98ad385c7")
        print(playlist)
        self.assertTrue(playlist)

    def test_playlist_items(self):
        playlist_items = cloud.playlist_items(playlist_uid="98015ae9c2bb4d0d986693d98ad385c7", page="1", count="10", sort="name+asc")
        print(playlist_items)
        self.assertTrue(playlist_items)

    def test_create_playlist(self):
        created_playlist = cloud.create_playlist(name="Demo Playlist", paths="/VZMOBILE/My HTC6525LVW/01 - Afghan Jalebi - Ya Baba MyMp3Song.Com.mp3", type="music")
        print(created_playlist)
        self.assertTrue(created_playlist)

    def test_create_playlist_items(self):
        created_playlist_items = cloud.create_playlist_items(playlist_uid="98015ae9c2bb4d0d986693d98ad385c7", playlist_items= ["demo_item1", "demo_item2"])
        print(created_playlist_items)
        self.assertTrue(created_playlist_items)

    def test_create_playlist_items(self):
        created_playlist_items = cloud.create_playlist_items(playlist_uid="98015ae9c2bb4d0d986693d98ad385c7", playlist_items= ["demo_item1", "demo_item2"])
        print(created_playlist_items)
        self.assertTrue(created_playlist_items)

    def test_delete_playlist_item(self):
        deleted_playlist_items = cloud.delete_playlist_item(playlist_uid="98015ae9c2bb4d0d986693d98ad385c7", item_uid="")
        print(deleted_playlist_items)
        self.assertTrue(deleted_playlist_items)

    def test_delete_playlist(self):
        deleted_playlist = cloud.delete_playlist(playlist_uid="98015ae9c2bb4d0d986693d98ad385c7")
        print(deleted_playlist)
        self.assertTrue(deleted_playlist)

    def test_update_playlist(self):
        update_playlist = cloud.update_playlist(playlist_uid="98015ae9c2bb4d0d986693d98ad385c7", name="Updated Demo Playlist", type="music")
        print(update_playlist)
        self.assertTrue(update_playlist)

    def test_update_playlist_def(self):
        update_playlist_def = cloud.update_playlist_def( playlist_uid="98015ae9c2bb4d0d986693d98ad385c7", name="Updated Demo Playlist", paths="/VZMOBILE/My HTC6525LVW/01 - Afghan Jalebi - Ya Baba MyMp3Song.Com.mp3", type="music")
        print(update_playlist_def)
        self.assertTrue(update_playlist_def)


if __name__ == '__main__':
    del sys.argv[1:]
    unittest.main()