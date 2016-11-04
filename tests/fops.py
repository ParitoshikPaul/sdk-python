#!/usr/bin/env python

#hack for now, need to figure out install or relative usage
import sys

sys.path.append("../sdk")

from thingspace.exceptions.CloudError import CloudError
from thingspace.cloud import Cloud
cloud = Cloud(
    client_key='KHFh8IEPpWF6p3elo6xMBNT5jyQa',
    client_secret='MNxyUF2TQVTcZzI_z_mhHM3DZ3Qa',
    callback_url='http://127.0.0.1:8000/token',
    auth_token='ZSTCDZLBGDANGUY2QOR6JDVYZ4PPUQE2SQTL5OYYP35RUGPATCUNJNGYCU3QO4RKEWLEECOJPIM5LRA66CM7MBG2OILIKWSOEWCH35EBNRQPZRDATMAOXGSYAETBMJO3X7PHSCCTO72SRXKE2OCFF7X5G6SM6GYZGPZOQ2OJ3T6CGIZLK3BARPHEENKFHJ4WUZ2GKZ44CZ6XYRI3FECQTGZEHYZUVL3BSHRPLKBCLC3RDERH75NXPJJ5WDYGO7I2XVYQW3S5H7GDGPUJMBFDBK3Y5U7VRXWU2JEAP7H6ZQJM4LYOHNDZXDYCEMZLVXMY2DPHPVEXKV4ULZPUP56ISYQCLDGDCVHDFW6YX53ZYQOEGIJKELZWZM7HJMUWD2QE'
)

try:
    # regular fullview
    print('regular fullview')
    files, empty_folders, etag = cloud.fullview()
    print(files, empty_folders, etag)

    #delta fullview
    print('\n\n\n\n\n\n delta fullview')
    files, empty_folders, etag = cloud.fullview(etag)
    print(files, empty_folders, etag)

except CloudError as e:
    print(e)

try:
    #metadata at root
    print('\n\n\n\n\n\n metadata at root')
    files, folders = cloud.metadata()
    print(files, folders)

    #metadata inside VZMOBILE
    print('\n\n\n\n\n\n metadata at at /VZMOBILE')
    files, folders = cloud.metadata('/VZMOBILE')
    print(files, folders)

except CloudError as e:
    print(e.json)

#big_file = open('sample-files/pycharm-community-2016.2.3.dmg', 'rb')
small_file = open('sample-files/ScreenShare.dmg', 'rb')

try:
    print('\n\n\n\n\n\n uploading big small file')
    file_uploaded = cloud.upload(small_file, '/VZMOBILE/ryantest/9')
    print(file_uploaded)

    #print('\n\n\n\n\n\n uploading big file')
    #file_uploaded = cloud.upload(big_file, '/VZMOBILE/ryantest/9')
    #print(file_uploaded)
except CloudError as e:
    print(e, e.status_code, e.json)

authorize_url = cloud.get_authorize_url()
print(authorize_url)

