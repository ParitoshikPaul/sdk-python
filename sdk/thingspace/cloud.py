import os

from thingspace.env import Env
from thingspace.exceptions.CloudError import CloudError
from thingspace.models.Account import Account
from thingspace.models.factories.FopsFactories import FopsFactories
from thingspace.operations.fops import Fops
from thingspace.operations.oauth import Oauth
from thingspace.operations.upload import Upload

from thingspace.packages.requests.requests import Request, Session


class Cloud(Oauth, Upload, Fops):

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

    def account(self):
        resp = self.networker(Request(
            'GET',
            str(Env.api_cloud + '/account'),
            headers={
                "Authorization": "Bearer " + self.auth_token
            }
        ))

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

        resp = self.networker(Request(
            'GET',
            str(Env.api_cloud + '/search'),
            params=queryparams,
            headers={
                "Authorization": "Bearer " + self.auth_token
            }
        ))

        # handle other error codes here needed TODO

        json = resp.json()
        files = FopsFactories.files_from_json(self, json['searchResults'].get('file', []))
        folders = FopsFactories.folders_from_json(json['searchResults'].get('folder', []))

        return files, folders

    def networker(self, request, bubble=True, retry=False):
        s = Session()
        prepped = request.prepare()
        resp = s.send(prepped)

        if resp.status_code == 503:
            raise CloudError('Service is unavailable', None, resp.status_code)
        elif resp.status_code >= 504:
            raise CloudError('Gateway timeout', None, resp.status_code)
        elif resp.status_code >= 500:
            try:
                raise CloudError('Server error', resp.json(), resp.status_code)
            except ValueError:
                raise CloudError('Server error', None, resp.status_code)



        #automatic refresh
        if resp.status_code == 401 and self.authenticated and bubble and self.refresh_token:
            raise CloudError('Unauthorized request', resp.json(), resp.status_code)
        elif resp.status_code == 401:
            raise CloudError('Unauthorized request', resp.json(), resp.status_code)


        return resp