#hack for now, need to figure out install or relative usage
import sys
sys.path.append("../sdk")
import argparse
from thingspace.cloud import Cloud

class Utils:

    @staticmethod
    def cloud_from_args():
        parser = argparse.ArgumentParser(description='Test harness for the python SDK')
        parser.add_argument('access_token',
                            help='access token')
        parser.add_argument('refresh_token',
                            help='refresh_token')
        args = parser.parse_args()
        return args

    @staticmethod
    def create_cloud(access_token, refresh_token):
        cloud = Cloud(
            client_key='KHFh8IEPpWF6p3elo6xMBNT5jyQa',
            client_secret='MNxyUF2TQVTcZzI_z_mhHM3DZ3Qa',
            callback_url='http://127.0.0.1:8000/token',
            access_token=access_token,
            refresh_token=refresh_token,
        )
        return cloud


    @staticmethod
    def cloud():
        args = Utils.cloud_from_args();
        return Utils.create_cloud(args.access_token, args.refresh_token)


    @staticmethod
    def assert_is_file(unit_tester, file):
        unit_tester.assertTrue(file.name)
        unit_tester.assertTrue(file['name'])

        unit_tester.assertTrue(file.parent_path)
        unit_tester.assertTrue(file['parent_path'])

        unit_tester.assertTrue(file.fullpath())

    @staticmethod
    def assert_is_files(unit_tester, files):

        for file in files:
            Utils.assert_is_file(unit_tester, file)


    @staticmethod
    def assert_is_folder(unit_tester, folder):
        unit_tester.assertTrue(folder.name)
        unit_tester.assertTrue(folder['name'])
        unit_tester.assertTrue(folder.parent_path)
        unit_tester.assertTrue(folder['parent_path'])

        unit_tester.assertTrue(folder.fullpath())

    @staticmethod
    def assert_is_folders(unit_tester, folders):
        for folder in folders:
            Utils.assert_is_folder(unit_tester, folder)


    @staticmethod
    def assert_is_playlist(unit_tester, playlist):
        for playlist in playlist:
            Utils.assert_is_file(unit_tester, playlist)



