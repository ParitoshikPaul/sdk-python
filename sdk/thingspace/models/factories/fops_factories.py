from thingspace.models.cloud_file import CloudFile
from thingspace.models.cloud_folder import CloudFolder

class FopsFactories:

    @staticmethod
    def file_from_json(cloud, json):

        return CloudFile(cloud, json)

    @staticmethod
    def files_from_json(cloud, json):
        files = []
        for file in json:
            files.append(FopsFactories.file_from_json(cloud, file))
        return files

    @staticmethod
    def folder_from_json(json):
        return CloudFolder(json)

    @staticmethod
    def folders_from_json(json):
        folders = []
        for folder in json:
            folders.append(FopsFactories.folder_from_json(folder))
        return folders
