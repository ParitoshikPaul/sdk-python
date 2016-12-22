#!/usr/bin/env python
import sys
from utils import Utils
import unittest
from thingspace.exceptions import CloudError, NotFoundError

cloud = Utils.cloud()

class Playlist(unittest.TestCase):

    def test_playlists(self):

        playlist = cloud.playlists(type='music', page='1', count='1', sort='name+asc')
        self.assertTrue(playlist)

    def test_playlist(self):
        playlist = cloud.playlist(playlist_uid="")
        print(playlist)
        self.assertTrue(playlist)

if __name__ == '__main__':
    del sys.argv[1:]
    unittest.main()