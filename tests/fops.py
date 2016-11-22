#!/usr/bin/env python
import sys
from utils import Utils
import unittest
from thingspace.exceptions import CloudError, NotFoundError

cloud = Utils.cloud()

class TestFops(unittest.TestCase):

    def test_fullview(self):
        #regular fullview
        files, empty_folders, etag1, deleted = cloud.fullview()
        self.assertTrue(files);
        self.assertTrue(etag1);

        file = files[0]

        #test dot and array index notation
        self.assertTrue(file.system_attributes)
        self.assertTrue(file['system_attributes'])
        self.assertTrue(file['system_attributes'].mime_type)
        self.assertTrue(file['system_attributes']['mime_type'])

        #get download urls via both interfaces
        self.assertTrue(file.download_url())
        self.assertTrue(cloud.download_url(file))

        with self.assertRaises(ValueError):
            cloud.download_url(None)

        #delta
        response = cloud.fullview(etag=etag1)
        self.assertFalse(response.files)
        self.assertEqual(response.etag,etag1)

        #bad delta not working currently
        #with self.assertRaises(CloudError):
            #cloud.fullview(etag='bad_etag')

    def test_metadata(self):

        #make sure
        files, folders = cloud.metadata()
        self.assertTrue(folders)

        with self.assertRaises(NotFoundError):
            cloud.metadata(path='/path/doesnt/exist')


    def test_account(self):
        account = cloud.account()
        self.assertTrue(account)

    def test_search(self):
        files, folders = cloud.search(query='extension:jpg')
        self.assertTrue(files[0])

    def test_folder_create_delete(self):
        cloud.create_folder('/VZMOBILE/auto_test_folder')
        folder = cloud.create_folder('/VZMOBILE/auto_test_folder', override='overwrite')
        print(folder)
        self.assertTrue(folder)
        cloud.delete(folder, purge=True)

if __name__ == '__main__':
    del sys.argv[1:]
    unittest.main()


