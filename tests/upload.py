#!/usr/bin/env python
import sys

from utils import Utils
from thingspace.exceptions import NotFoundError
import unittest

cloud = Utils.cloud()

class TestUpload(unittest.TestCase):

    def test_upload_copy_delete(self):
        small_file = open('sample-files/ScreenShare.dmg', 'rb')
        file_uploaded = cloud.upload(small_file, '/VZMOBILE')
        Utils.assert_is_file(self, file_uploaded)


        #copy file
        copied = cloud.copy(file_uploaded, '/VZMOBILE/ScreenShare_copy_test.dmg')
        Utils.assert_is_file(self, copied)

        #move one of the files
        copied = cloud.move(copied, '/VZMOBILE/ScreenShare_copy_moved.dmg')
        print(copied)
        Utils.assert_is_file(self, copied)

        #cleanup both files by reference and path
        cloud.delete('/VZMOBILE/ScreenShare.dmg')
        cloud.delete(copied)

        #make sure it was deleted
        with self.assertRaises(NotFoundError):
            cloud.delete(file_uploaded)



    def test_open_by_name(self):

        file_uploaded = cloud.upload('sample-files/ScreenShare.dmg', '/VZMOBILE')
        print(file_uploaded)
        self.assertTrue(file_uploaded)

        #delete file by file reference now
        cloud.delete(file_uploaded.parent_path + "/" + file_uploaded.name, purge=True)

        with self.assertRaises(NotFoundError):
            cloud.delete(file_uploaded)

if __name__ == '__main__':
    del sys.argv[1:]
    unittest.main()


