#!/usr/bin/env python

#hack for now, need to figure out install or relative usage
import sys
sys.path.append("../sdk")


from thingspace.cloud import Cloud
cloud = Cloud(
    client_key='KHFh8IEPpWF6p3elo6xMBNT5jyQa',
    client_secret='MNxyUF2TQVTcZzI_z_mhHM3DZ3Qa',
    callback_url='http://127.0.0.1:8000/token',
    auth_token='7VE67LQ5ZLP6CEA4GQ266JAAPQRH2UW5IYBTP6BP7DSB77YPJUFUFXEG62BLZS5TEGTMFUJMPV25R3C5QXURAVZMQEMSFSSPIWJTT4AV37U6XMVSWY5L5FTUHFUHTM3J7HVNSX4MBLU6UWI7F4YZ3JHU3A5GYZEIC73C5DTEPFUV3LHBM7VE4EWTYPON2CS72D7TSS5FSWFLRZU7KWUVPVAYDNUUDVDJMAOIZ3YOWUFGAOIXHTYQLT2LZIFGTACU7IIR3UFFOTA5BNUFZVAZI2O5QNA7KLDPUGS3ZM22LTTHZ3IP2OHQZTJXW74FHYFCMBXKIXXZABHL3PCZZ6GRS7AHM3C6VEMEPT6ALGM2YLNJ6EPSDTVEMD7NX5AQCWER'
)

file = open('sample-files/pycharm-community-2016.2.3.dmg', 'rb')
cloud.upload(file, '/VZMOBILE')

file = open('sample-files/ScreenShare.dmg', 'rb')
cloud.upload(file, '/VZMOBILE')

authorize_url = cloud.get_authorize_url()
print(authorize_url)

