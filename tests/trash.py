#!/usr/bin/env python
import sys
from utils import Utils
import unittest

cloud = Utils.cloud()

class TestTrash(unittest.TestCase):

    def test_trash_ops(self):
        files, folders = cloud.trash()
        print(files)
        print(folders)

        Utils.assert_is_files(self, files)
        Utils.assert_is_folders(self, folders)

    def test_empty_trash(self):
        file_uploaded = cloud.upload('sample-files/ScreenShare.dmg', '/VZMOBILE', name="test_restore.dmg")
        cloud.empty_trash()

        files, folders = cloud.trash()
        self.assertFalse(files)
        self.assertFalse(folders)

    def test_restore_trash(self):
        file_uploaded = cloud.upload('sample-files/ScreenShare.dmg', '/VZMOBILE', name="test_restore.dmg")
        Utils.assert_is_file(self, file_uploaded)
        cloud.delete(file_uploaded)
        cloud.restore(file_uploaded)

        file = cloud.file_metadata('/VZMOBILE/test_restore.dmg')
        print('file metadata' + str(file))




if __name__ == '__main__':
    del sys.argv[1:]
    unittest.main()
