from thingspace.env import Env
from thingspace.exceptions import CloudError
from thingspace.exceptions import UnauthorizedError
from thingspace.models.account import Account
from thingspace.models.factories.FopsFactories import FopsFactories
from thingspace.operations.fops import Fops
from thingspace.operations.oauth import Oauth
from thingspace.operations.upload import Upload

from thingspace.packages.requests.requests import Request, Session
import time


class Cloud(Oauth, Upload, Fops):

    def __init__(self,
                 client_key,
                 client_secret,
                 callback_url,
                 access_token=None,
                 refresh_token=None,
                 on_refreshed=None,
                 ):

        self.client_key = client_key
        self.client_secret = client_secret
        self.callback_url = callback_url
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.on_refreshed = on_refreshed

        # authenticated if we have an auth token
        self.authenticated = self.access_token is not None

    def account(self):
        resp = self.networker(Request(
            'GET',
            str(Env.api_cloud + '/account'),
            headers={
                "Authorization": "Bearer " + self.access_token
            }
        ))

        # handle other error codes here needed TODO
        json = resp.json()

        return Account(json)

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
                "Authorization": "Bearer " + self.access_token
            }
        ))

        # handle other error codes here needed TODO
        if resp.status_code != 200:
            print(resp.status_code)
            print(resp.text)
            raise CloudError('Could not get search results', response=resp)

        json = resp.json()



        files = FopsFactories.files_from_json(self, json['searchResults'].get('file', []))
        folders = FopsFactories.folders_from_json(json['searchResults'].get('folder', []))

        return files, folders

    def networker(self, request, auto_refresh=True, retry=False):
        s = Session()
        prepped = request.prepare()
        resp = s.send(prepped)

        if resp.status_code == 503:
            raise CloudError('Service is unavailable',  response=resp)
        elif resp.status_code == 504:
            raise CloudError('Gateway timeout', response=resp)
        elif resp.status_code >= 500:
            raise CloudError('Server error', response=resp)

        #automatic refresh logic
        if resp.status_code == 401 and self.authenticated and auto_refresh and self.refresh_token:
            try:
                refresh_tokens = self.refresh()
                print('refresh worked:' + str(refresh_tokens))
                #update access token of course
                request.headers['Authorization'] = "Bearer " + self.access_token
                return self.networker(request, auto_refresh=False)
            except CloudError as error:
                print('refresh failed:' + str(error.response.text))
                raise UnauthorizedError('Unauthorized request', response=error.response)
        elif resp.status_code == 401:
            raise UnauthorizedError('Unauthorized request', response=resp)

        return resp
