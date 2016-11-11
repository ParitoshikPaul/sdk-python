import os

from thingspace.env import Env
from thingspace.exceptions import CloudError
from thingspace.models.upload_intent import UploadIntent
from thingspace.models.factories.FopsFactories import FopsFactories
from thingspace.packages.requests.requests import Request
from thingspace.packages.requests.requests.packages.urllib3.packages import six
from thingspace.utils.hasher import Hasher


class Upload:

    def upload(self, file, upload_path, name=None, chunked=False, chunk_size=Env.chunked_upload_size):

        if isinstance(file, six.string_types):
            with open(file, 'rb') as file:
                return self.__upload_handler(file, upload_path, name, chunked, chunk_size)
        else:
            return self.__upload_handler(file, upload_path, name, chunked, chunk_size)


    def __upload_handler(self, file, upload_path, name, chunked, chunk_size):
        checksum = Hasher.hashfile(file)
        size = os.fstat(file.fileno()).st_size
        fname = name if name else os.path.basename(file.name)

        if size >= 104857600:
            chunked = True

        intent = self.fileUploadIntent(size, chunked, fname, upload_path, checksum)
        file.seek(0)
        if chunked:
            return self.__chunked_facade(intent, file, chunk_size)
        else:
            return self.__unchunked_facade(intent, file)


    def __chunked_facade(self, intent, file, chunk_size):
        buf = file.read(chunk_size)
        chunk = 1
        while len(buf) > 0:
            resp = self.networker(Request(
                'POST',
                intent.uploadurls['uploadurl'] + "&offset=" + str(chunk),
                data=buf,
                headers={
                    "Authorization": "Bearer " + self.access_token,
                    'Content-Type': 'application/octet-stream',
                }
            ))

            if resp.status_code != 201:
                raise CloudError('Could not upload chunk', response=resp)
            chunk += 1
            buf = file.read(chunk_size)
        return self.commit_chunked_upload(intent)

    def __unchunked_facade(self, intent, file):
        resp = self.networker(Request(
            'POST',
            intent.uploadurls['uploadurl'],
            data=file,
            headers={
                "Authorization": "Bearer " + self.access_token,
                'Content-Type': 'application/octet-stream',
            }
        ))
        json = resp.json()
        return FopsFactories.file_from_json(self, json['file'])

    def fileUploadIntent(self, size, chunk, name, path, checksum):
        # add mandatory params
        queryparams = {
            'size': size,
            'chunk': str(chunk).lower(),  # need true or false here cant have caps
            'name': name,
            'path': path,
            'checksum': checksum.lower(),
        }

        resp = self.networker(Request(
            'GET',
            str(Env.api_cloud + '/fileupload/intent'),
            params=queryparams,
            headers={
                "Authorization": "Bearer " + self.access_token
            }
        ))

        # handle other error codes here needed TODO
        if resp.status_code != 200:
            raise CloudError('Could not start upload intent', response=resp)

        json = resp.json()
        return UploadIntent(checksum, json)

    def commit_chunked_upload(self, intent):
        resp = self.networker(Request(
            'POST',
            intent.uploadurls['commiturl'],
            headers={
                "Authorization": "Bearer " + self.access_token
            }
        ))

        json = resp.json()
        if resp.status_code != 201:
            raise CloudError('Could not finalize chunked upload', response=resp)
        return FopsFactories.file_from_json(self, json['file'])