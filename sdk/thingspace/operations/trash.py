import collections

from thingspace.env import Env
from thingspace.exceptions import CloudError, NotFoundError
from thingspace.models.factories.FopsFactories import FopsFactories
from thingspace.operations.fops import Fops
from thingspace.packages.requests.requests import Request



class Trash():

    def empty_trash(self, virtualfolder="VZMOBILE"):
        resp = self.networker(Request(
            'DELETE',
            Env.api_cloud + '/trash',
            params={
                'virtualfolder': virtualfolder
            },
            headers={
                "Authorization": "Bearer " + self.access_token
            }
        ))

        if resp.status_code == 404:
            raise NotFoundError("virtual folder not found", response=resp)

        if resp.status_code != 200:
            raise CloudError('Could not empty the trash', response=resp)

        return

    def restore(self, file_or_path):
        file_path = Fops.file_or_path_to_path(file_or_path)

        resp = self.networker(Request(
            'POST',
            Env.api_cloud + '/fops/restore',
            json={
                "path": [file_path]
            },
            headers={
                "Authorization": "Bearer " + self.access_token
            }
        ))

        if resp.status_code == 404:
            raise NotFoundError("file not found, could not restore", response=resp)

        if resp.status_code != 204:
            raise CloudError("Could not restore file", response=resp)

        return


    def trash(self, virtualfolder="VZMOBILE", sort=None, page=1, count=20, deep=False, filter=None):
        if not virtualfolder:
            raise ValueError("virtualfolder must be provided")
        if not page or page < 1:
            raise ValueError("page must be provided and greater than 1")
        if not count or count < 1 or count > 100:
            raise ValueError("count must be provided and greater than 0 and less than 100")

        # add mandatory params
        queryparams = {
            'virtualfolder': virtualfolder,
            'count': count,
            'page': page,
            'deep': deep,
        }

        if sort:
            queryparams['sort'] = sort

        if filter:
            queryparams['filter'] = filter

        resp = self.networker(Request(
            'GET',
            Env.api_cloud + '/trash',
            params=queryparams,
            headers={
                "Authorization": "Bearer " + self.access_token
            }
        ))
        if resp.status_code == 404:
            raise CloudError('virtualfolder not found, could not get trash can items', response=resp)

        if resp.status_code != 200:
            raise CloudError('Could not get trash can items', response=resp)

        files = FopsFactories.files_from_json(self, resp.json()['trashCan'].get('file', []))
        folders = FopsFactories.folders_from_json(resp.json()['trashCan'].get('folder', []))

        TrashResponse = collections.namedtuple('TrashResponse', 'files folders')

        return TrashResponse(files, folders)
