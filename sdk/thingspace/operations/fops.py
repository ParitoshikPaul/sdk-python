import collections
from thingspace.models.cloud_file import CloudFile
from thingspace.models.cloud_folder import CloudFolder
from thingspace.packages.requests.requests.packages.urllib3.packages.six.moves import urllib

from thingspace.env import Env
from thingspace.exceptions import CloudError, NotFoundError
from thingspace.exceptions import OutOfSyncError
from thingspace.models.factories.FopsFactories import FopsFactories
from thingspace.packages.requests.requests import Request
from thingspace.packages.requests.requests.packages.urllib3.packages import six
from thingspace.utils.path import Path


class Fops():

    OVERWRITE = 'overwrite'
    MODIFY = 'modify'

    def metadata(self, path='/'):
        resp = self.networker(Request(
            'GET',
            str(Env.api_cloud + '/metadata' + path),
            headers={
                "Authorization": "Bearer " + self.access_token
            }
        ))

        if resp.status_code == 404:
            raise NotFoundError("path not found", response=resp)

        MetadataResponse = collections.namedtuple('MetadataResponse', 'files folders')

        json = resp.json()

        files = FopsFactories.files_from_json(self, json['folder'].get('file', []))
        folders = FopsFactories.folders_from_json(json['folder'].get('folder', []))

        return MetadataResponse(files, folders)


    def file_metadata(self, path):
        resp = self.networker(Request(
            'GET',
            str(Env.api_cloud + '/metadata' + path),
            headers={
                "Authorization": "Bearer " + self.access_token
            }
        ))

        if resp.status_code == 404:
            raise NotFoundError("path not found", response=resp)


        json = resp.json()

        file = FopsFactories.file_from_json(self, json['file'])

        return file

    def fullview(self, etag=None):
        if not self.authenticated:
            return None

        headers = {
            "Authorization": "Bearer " + self.access_token
        }

        if etag is not None:
            headers["X-Header-ETag"] = etag

        resp = self.networker(Request(
            'GET',
            Env.api_url + '/cloud/' + Env.api_version + '/fullview',
            headers=headers
        ))

        FullviewResponse = collections.namedtuple('FullviewResponse', 'files empty_folders etag deleted')

        # fullview is in sync, no changes
        if resp.status_code == 412:
            return FullviewResponse([], [], etag, [])

        # fullview is too far out of sync
        if resp.status_code == 205:
            raise OutOfSyncError("You are too far out of sync, please call fullview again with no etag", response=resp)

        json = resp.json()

        files = FopsFactories.files_from_json(self, json['data'].get('file', []))
        empty_folders = FopsFactories.folders_from_json(json['data'].get('folder', []))
        etag = resp.headers['X-Header-ETag']
        try:
            deleted = json['data']['deleted']['path']
        except KeyError:
            deleted = []

        return FullviewResponse(files, empty_folders, etag, deleted)



    def download_url(self, file_or_path):
        file_path = Fops.file_or_path_to_path(file_or_path)

        req = Request(
            'GET',
            Env.api_cloud + '/files' + urllib.parse.quote(file_path),
            params={
                'access-token': self.access_token
            }
        )
        prepped = req.prepare()
        return prepped.url

    def delete(self, file_or_path, purge=False):
        file_path = Fops.file_or_path_to_path(file_or_path)
        resp = self.networker(Request(
            'DELETE',
            Env.api_cloud + '/fops/delete',
            params={
                'path': file_path,
                'purge': purge
            },
            headers={
                "Authorization": "Bearer " + self.access_token
            }
        ))

        if resp.status_code == 404:
            raise NotFoundError("file or folder not found", response=resp)

        if resp.status_code != 200:
            raise CloudError("Could not delete file or folder", response=resp)

        return

    def create_folder(self, path, override=None):
        if path is None:
            raise ValueError('Path must not be None')
        if override is not None and override is not Fops.OVERWRITE and override is not Fops.MODIFY:
            raise ValueError('override may only be None, ' + Fops.OVERWRITE + ', or ' + Fops.MODIFY)

        parent_path, name = Path.fullpathToNameAndPath(path)

        #add mandatory
        body = {
            'path': parent_path,
            'name': name,
        }

        #add optional
        if override:
            body['override'] = override

        resp = self.networker(Request(
            'POST',
            Env.api_cloud + '/fops/createfolder',
            json=body,
            headers={
                "Authorization": "Bearer " + self.access_token
            }
        ))

        if resp.status_code == 404:
            raise NotFoundError("path not found", response=resp)

        if resp.status_code != 201 and resp.status_code != 200:
            raise CloudError("Could not create the folder", response=resp)

        return FopsFactories.folder_from_json(resp.json()['folder'])

    @staticmethod
    def file_or_path_to_path(file_or_path):
        if isinstance(file_or_path, (CloudFile, CloudFolder)):
            return file_or_path.parent_path + '/' + file_or_path.name
        elif isinstance(file_or_path, six.string_types):
            return file_or_path
        else:
            raise ValueError("file or path must be provided")