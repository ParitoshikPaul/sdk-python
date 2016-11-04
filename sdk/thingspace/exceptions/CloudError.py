class CloudError(Exception):
    def __init__(self, message, json=None, status_code=None):
        super(CloudError, self).__init__(message)

        self.json = json
        self.status_code = status_code

