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
        cloud.empty_trash()

        files, folders = cloud.trash()
        self.assertFalse(files)
        self.assertFalse(folders)


if __name__ == '__main__':
    del sys.argv[1:]
    unittest.main()
