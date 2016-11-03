import hashlib
import os

from thingspace.env import Env
from thingspace.exceptions.CloudError import CloudError
from thingspace.exceptions.OutOfSyncError import OutOfSyncError
from thingspace.models.Account import Account
from thingspace.models.factories.FopsFactories import FopsFactories

from thingspace.packages.requests.requests import Request, Session
from thingspace.utils.hasher import Hasher


class Cloud:

    def __init__(self,
                 client_key,
                 client_secret,
                 callback_url,
                 auth_token=None,
                 refresh_token=None
                 ):
        self.client_key = client_key
        self.client_secret = client_secret
        self.callback_url = callback_url
        self.auth_token = auth_token
        self.refresh_token = refresh_token

        # authenticated if we have an auth token
        self.authenticated = self.auth_token is not None

    def get_authorize_url(self):
        req = Request(
            'GET',
            str(Env.api_url + '/cloud/' + Env.api_version + '/oauth2/authorize'),
            params={
                'client_id': self.client_key,
                'redirect_uri': self.callback_url,
                'response_type': 'code',
            }
        )
        prepped = req.prepare()
        return prepped.url

    def token(self, auth_code):
        s = Session()
        req = Request(
            'POST',
            str(Env.api_url + '/cloud/' + Env.api_version + '/oauth2/token'),
            data={
                'client_id': self.client_key,
                'client_secret': self.client_secret,
                'redirect_uri': self.callback_url,
                'code': auth_code,
                'grant_type': 'authorization_code',
            }
        )
        prepped = req.prepare()

        resp = s.send(prepped)
        json = resp.json()
        # need to handle error cases
        self.auth_token = json['access_token']
        self.refresh_token = json['refresh_token']
        self.authenticated = True

        return json

    def upload(self, file, upload_path, name=None):
        checksum = Hasher.hashfile(file)

        print(checksum)
        size = file.tell()
        fname = name if name else os.path.basename(file.name)
        print(fname)
        print(size)
        print(type(size))
        if size < 104857600:
            chunked = False
        else:
            chunked = True

        intent = self.fileUploadIntent(size, chunked, fname, upload_path, checksum)
        print(intent)

    def fileUploadIntent(self, size, chunk, name, path, checksum):
        #add mandatory params
        queryparams = {
            'size' : size,
            'chunk': str(chunk).lower(), #need true or false here cant have caps
            'name': name,
            'path': path,
            'checksum': checksum.lower(),
        }

        s = Session()
        req = Request(
            'GET',
            str(Env.api_cloud + '/fileupload/intent'),
            params=queryparams,
            headers={
                "Authorization": "Bearer " + self.auth_token
            }
        )
        prepped = req.prepare()
        resp = s.send(prepped)

        # handle other error codes here needed TODO

        json = resp.json()
        return json

    def account(self):
        s = Session()
        req = Request(
            'GET',
            str(Env.api_cloud + '/account'),
            headers={
                "Authorization": "Bearer " + self.auth_token
            }
        )

        prepped = req.prepare()
        resp = s.send(prepped)

        # handle other error codes here needed TODO

        json = resp.json()

        return Account(**json)

    def search(self, query=None, sort=None, virtualfolder="VZMOBILE", page=1, count=20):
        if not query:
            raise ValueError("a query must be provided")
        if not virtualfolder:
            raise ValueError("virtualfolder must be provided")
        if not page or page < 1:
            raise ValueError("page must be provided and greater than 1")
        if not count or count < 1 or count > 100:
            raise ValueError("count must be provided and greater than 0 and less than 100")

        #add mandatory params
        queryparams = {
            'query' : query,
            'virtualfolder': virtualfolder,
            'count': count,
            'page': page,
        }

        if sort:
            queryparams['sort'] = sort

        s = Session()
        req = Request(
            'GET',
            str(Env.api_cloud + '/search'),
            params=queryparams,
            headers={
                "Authorization": "Bearer " + self.auth_token
            }
        )

        prepped = req.prepare()
        resp = s.send(prepped)

        # handle other error codes here needed TODO

        json = resp.json()
        files = FopsFactories.files_from_json(self, json['searchResults'].get('file', []))
        folders = FopsFactories.folders_from_json(json['searchResults'].get('folder', []))

        return files, folders

    def metadata(self, path='/'):

        s = Session()
        req = Request(
            'GET',
            str(Env.api_cloud + '/metadata' + path),
            headers={
                "Authorization": "Bearer " + self.auth_token
            }
        )

        prepped = req.prepare()
        resp = s.send(prepped)

        if resp.status_code == 404:
            raise CloudError("path not found")

        #handle other error codes here needed TODO

        json = resp.json()

        print(json)

        files = FopsFactories.files_from_json(self, json['folder'].get('file', []))
        folders = FopsFactories.folders_from_json(json['folder'].get('folder', []))

        return files, folders

    def fullview(self, etag=None):
        if not self.authenticated:
            return None

        headers = {
            "Authorization": "Bearer " + self.auth_token
        }

        if etag is not None:
            headers["X-Header-ETag"] = etag

        s = Session()
        req = Request(
            'GET',
            Env.api_url + '/cloud/' + Env.api_version + '/fullview',
            headers=headers
        )

        prepped = req.prepare()
        resp = s.send(prepped)

        #fullview is in sync, no changes
        if resp.status_code == 412:
            return [], [], etag

        #fullview is too far out of sync
        if resp.status_code == 205:
            raise OutOfSyncError("You are too far out of sync, please call fullview again with no etag")

        #handle other error codes here needed TODO

        json = resp.json()

        files = FopsFactories.files_from_json(self, json['data'].get('file', []))
        folders = FopsFactories.folders_from_json(json['data'].get('folder', []))
        etag = resp.headers['X-Header-ETag']

        return files, folders, etag

    def download_url(self, file=None, path=None):

        if file is not None:
            file_path = file.parentPath + '/' + file.name
        elif path is not None:
            file_path = path
        else:
            raise ValueError("file or path must be provided")

        req = Request(
            'GET',
            Env.api_cloud + '/files' + file_path,
            params={
                'access-token': self.auth_token
            }
        )
        prepped = req.prepare()
        return prepped.url
