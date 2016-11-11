from thingspace.packages.requests.requests.packages.urllib3.packages.six.moves import urllib

from thingspace.env import Env
from thingspace.exceptions import CloudError, NotFoundError
from thingspace.exceptions import OutOfSyncError
from thingspace.models.factories.FopsFactories import FopsFactories
from thingspace.packages.requests.requests import Request


class Fops():
    def metadata(self, path='/'):
        resp = self.networker(Request(
            'GET',
            str(Env.api_cloud + '/metadata' + path),
            headers={
                "Authorization": "Bearer " + self.access_token
            }
        ))

        json = resp.json()

        if resp.status_code == 404:
            raise NotFoundError("path not found", response=resp)

        # handle other error codes here needed TODO

        files = FopsFactories.files_from_json(self, json['folder'].get('file', []))
        folders = FopsFactories.folders_from_json(json['folder'].get('folder', []))

        return files, folders


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

        # fullview is in sync, no changes
        if resp.status_code == 412:
            return [], [], etag

        # fullview is too far out of sync
        if resp.status_code == 205:
            raise OutOfSyncError("You are too far out of sync, please call fullview again with no etag", response=resp)

        # handle other error codes here needed TODO

        json = resp.json()

        files = FopsFactories.files_from_json(self, json['data'].get('file', []))
        folders = FopsFactories.folders_from_json(json['data'].get('folder', []))
        etag = resp.headers['X-Header-ETag']

        return files, folders, etag


    def download_url(self, file=None, path=None):
        if file is not None:
            file_path = file.parent_path + '/' + file.name
        elif path is not None:
            file_path = path
        else:
            raise ValueError("file or path must be provided")

        req = Request(
            'GET',
            Env.api_cloud + '/files' + urllib.parse.quote(file_path),
            params={
                'access-token': self.access_token
            }
        )
        prepped = req.prepare()
        return prepped.url
