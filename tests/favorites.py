#!/usr/bin/env python
import sys
from utils import Utils
import unittest
from thingspace.exceptions import CloudError, NotFoundError

cloud = Utils.cloud()

class Favorites(unittest.TestCase):

    def test_favorites(self):
        favorites = cloud.favorites(virtual_folder="VZMOBILE", type="file", filetype="music")
        print(favorites)
        self.assertTrue(favorites)

    def test_favorites_update(self):
        favorites_update = cloud.updatefavorites(createversion="TRUE")
        print(favorites_update)
        self.assertTrue(favorites_update)

    def test_favorites_delete(self):
        favorites_delete = cloud.deletefavorites(uri="dv-file://d28d9f89d9224270a11410390177e5da:VZMOBILE/testGarima/systemattributes.xls", createversion="TRUE")
        print(favorites_delete)
        self.assertTrue(favorites_delete)

if __name__ == '__main__':
    del sys.argv[1:]
    unittest.main()