class CloudError(Exception):
    def __init__(self, message, response=None):
        super(CloudError, self).__init__(message)
        self.response = response


class OutOfSyncError(CloudError):
    pass


class UnauthorizedError(CloudError):
    pass


class ConflictError(CloudError):
    pass


class NotFoundError(CloudError):
    pass
