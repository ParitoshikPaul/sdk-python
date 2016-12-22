#!/usr/bin/env python
import sys
from utils import Utils
import unittest
from thingspace.exceptions import CloudError, NotFoundError

cloud = Utils.cloud()

class Playlist(unittest.TestCase):

    def test_playlists(self):

        playlist = cloud.playlists()
        self.assertTrue(playlist)

    def test_get_playlist_definition(self):
        playlist_def = cloud.get_playlist_definition()
        print(playlist_def)
        self.assertTrue(playlist_def)

if __name__ == '__main__':
    del sys.argv[1:]
    unittest.main()