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