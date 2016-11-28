#!/usr/bin/env python
import sys
from utils import Utils
import unittest
import time
cloud = Utils.cloud()

class TestOauth(unittest.TestCase):

    def test_refresh_manually(self):
        cloud.on_refreshed = None

        old_token = cloud.access_token
        refresh = cloud.refresh()
        print(refresh)
        self.assertTrue(refresh)
        self.assertNotEqual(refresh.access_token, old_token)


    def test_refresh_automatic(self):
        time.sleep(3)
        bad_token = 'bad_value'
        cloud.access_token = bad_token

        def callback(tokens):
            callback.cb_ran = True
            self.assertTrue(tokens)
            print('callback ran')
            print(tokens)

        callback.cb_ran = False

        #add the CB
        cloud.on_refreshed = callback

        #now call the api and see what happens
        account = cloud.account()
        self.assertTrue(account)
        self.assertNotEqual(cloud.access_token, bad_token)

        #assert that the callback was actually run
        self.assertTrue(callback.cb_ran)



if __name__ == '__main__':
    del sys.argv[1:]
    unittest.main()


