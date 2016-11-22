class Path:

    @staticmethod
    def fullpathToNameAndPath(fullpath):
        split = fullpath.rsplit('/', 1)
        parent_path = split[0]
        name = split[1]
        return parent_path, name