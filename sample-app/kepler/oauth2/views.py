from django.shortcuts import render, redirect
from thingspace.exceptions import CloudError


def index(request):

    if request.cloud.authenticated:
        return redirect('files')

    return render(request, 'oauth2/login.html', {'cloud': request.cloud})


def token(request):
    try:
        token_response = request.cloud.token(request.GET.get('code'))
        print('token response oauth view' + str(token_response))

    except CloudError:
        return render(request, 'oauth2/login.html', {'login_error': True, 'cloud': request.cloud})

    request.session['access_token'] = token_response.access_token
    request.session['refresh_token'] = token_response.refresh_token

    return redirect('files')


def refresh(request):
    token_response = request.cloud.refresh()

    request.session['access_token'] = token_response.access_token
    request.session['refresh_token'] = token_response.refresh_token

    return redirect('files')


# used to test automatic refreshing of access tokens
def invalidate_access_token(request):
    request.session['access_token'] = 'bad_token'
    return redirect(index)


def logout(request):
    request.session.flush()
    return redirect(index)
