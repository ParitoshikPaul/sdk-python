from sdk.thingspace.cloud import Cloud


def inject_cloud(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        # inject the cloud
        cloud = Cloud(
            client_key='KHFh8IEPpWF6p3elo6xMBNT5jyQa',
            client_secret='MNxyUF2TQVTcZzI_z_mhHM3DZ3Qa',
            callback_url='http://127.0.0.1:8000/token',
            auth_token=request.session.get('auth_token', None),
            refresh_token=request.session.get('refresh_token', None),
        )
        request.cloud = cloud

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware
