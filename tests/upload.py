#!/usr/bin/env python
import sys
from utils import Utils
import unittest

cloud = Utils.cloud()

class TestUpload(unittest.TestCase):

    def test_upload(self):
        small_file = open('sample-files/ScreenShare.dmg', 'rb')
        file_uploaded = cloud.upload(small_file, '/VZMOBILE')
        self.assertTrue(file_uploaded)

    def test_open_by_name(self):

        file_uploaded = cloud.upload('sample-files/ScreenShare.dmg', '/VZMOBILE')
        print(file_uploaded)
        self.assertTrue(file_uploaded)

if __name__ == '__main__':
    del sys.argv[1:]
    unittest.main()


